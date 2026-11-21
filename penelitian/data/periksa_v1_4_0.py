#!/usr/bin/env python3
"""Pemeriksa slop dan salah tulis untuk teks bahasa Indonesia (bahasa-skills).

Pemakaian:
  python3 periksa.py draf.md
  python3 periksa.py --ragam resmi laporan.md
  cat caption.txt | python3 periksa.py -
  python3 periksa.py --json --ketat draf.md

Tingkat temuan:
  KERAS   melanggar larangan atau kaidah. Tulis ulang kalimatnya.
  TINJAU  butuh penilaian. Sah bila ada alasannya; ubah bila hanya kebiasaan.

Kode mengikuti Sepuluh Larangan Keras di SKILL.md (L1 sampai L10), ditambah
EJ (ejaan dan kata baku), TB (tata bahasa), KS (konsistensi), dan PG (pola
pengganti). Teks di dalam backtick dan blok kode dilewati, jadi kutipan contoh
bisa dibungkus backtick. Skrip ini hanya mengenali pola yang tampak dari kata
dan tanda baca. Spesifisitas, dasar klaim, dan ketepatan ragam tetap harus dibaca
sendiri: nol temuan tidak berarti teks sudah baik.

Hanya memakai pustaka standar Python 3.8+.
"""

import argparse
import json
import re
import statistics
import sys

KERAS, TINJAU = "KERAS", "TINJAU"

# (kode, tingkat, nama, pola, saran)
ATURAN = [
    # ---- L1 pembuka klise
    ("L1", KERAS, "pembuka klise zaman",
     r"\b(di|pada) (tengah )?(era|zaman) (yang )?(digital|modern|globalisasi|teknologi|informasi|disrupsi"
     r"|serba \w+|sekarang|kini|saat ini|transformasi digital|kecerdasan buatan|industri 4\.0|society 5\.0)\b"
     r"|\bseiring (dengan )?(perkembangan|kemajuan|pesatnya|berkembangnya|berjalannya) "
     r"(teknologi|zaman|waktu|ilmu pengetahuan|era)\b"
     r"|\bdewasa ini\b|\b(tidak|tak) (dapat|bisa) di[pm]ungkiri\b"
     r"|\bdalam dunia [^.,\n]{1,30} yang (terus|semakin|kian|serba) \w+\b"
     r"|\bdi tengah (hiruk[- ]pikuk|gempuran|derasnya arus|pesatnya)\b",
     "Hapus. Mulai dari fakta, angka, atau situasi yang khas topik ini."),
    ("L1", KERAS, "pembuka pertanyaan basa-basi",
     r"\b(pernahkah|pernah ?kah|pernah (nggak|gak|enggak) sih) (anda|kamu|kalian|kita) "
     r"(bertanya-tanya|merasa|membayangkan|berpikir|mengalami)\b"
     r"|\btahukah (anda|kamu|kalian)\b"
     r"|\bsiapa (sih )?yang (tidak|tak|nggak|gak) (kenal|mengenal|tahu)\b"
     r"|\bseperti yang (sudah |telah )?kita (ketahui|tahu)\b",
     "Sebut faktanya langsung, atau ajukan pertanyaan yang memuat detail nyata."),
    # ---- L2 penutup ritual
    ("L2", KERAS, "penutup ritual",
     r"\bsemoga (artikel|tulisan|informasi|penjelasan|ulasan|panduan) ini\b|\bsemoga bermanfaat\b"
     r"|\bsebagai (kesimpulan|penutup)\b|\bkesimpulannya\b"
     r"|\bdemikian(lah)? (artikel|pembahasan|ulasan|penjelasan|informasi)\b"
     r"|\bitulah (tadi )?(pembahasan|ulasan|penjelasan|beberapa|sejumlah)\b"
     r"|\bselamat mencoba\b|\btunggu apa lagi\b|\bjangan ragu untuk\b"
     r"|\bmari (kita )?bersama-sama\b"
     r"|\bdengan memahami (hal-hal|hal|penjelasan|uraian) (di atas|ini|tersebut)\b"
     r"|\bsemua (kembali|tergantung) (ke|kepada|pada) (anda|kamu|preferensi|kebutuhan|pilihan)\b"
     r"|\bmasa depan [^.\n]{1,40} (terlihat|tampak) (sangat )?(cerah|menjanjikan)\b",
     "Akhiri di kalimat terakhir yang berisi informasi, atau beri satu langkah konkret."),
    # ---- L3 paralelisme negatif
    ("L3", KERAS, "paralelisme negatif",
     r"\b(bukan|tidak|tak|nggak|gak|enggak) (hanya|cuma|sekadar|sekedar|semata|melulu)\b"
     r"[^.!?\n]{0,120}?\b(tetapi|tapi|namun|melainkan)\b"
     r"|\bbukan (lagi )?(sekadar|sekedar)\b|\blebih dari (sekadar|sekedar)\b"
     r"|\bbukan lagi [^.!?\n]{1,60}?,? ?(melainkan|tetapi|tapi)\b"
     r"|\bbukan (soal|tentang)\b[^.!?\n]{0,80}?\b(melainkan|tapi|tetapi|ini) (soal|tentang)\b",
     "Pilih sisi yang benar dan tulis itu saja."),
    # ---- L5 kosakata slop
    ("L5", KERAS, "kosakata slop",
     r"\bhiruk[- ]pikuk\b|\bkrusial\b|\bmenyelami\b|\bmenyelam lebih dalam\b|\bmengupas tuntas\b"
     r"|\bmenggali lebih dalam\b|\bmenggarisbawahi\b|\bgarda terdepan\b|\bmercusuar\b|\bpermadani\b"
     r"|\blanskap (digital|bisnis|industri|persaingan|teknologi|pendidikan|politik|media|ekonomi|pemasaran|kompetitif)\b"
     r"|\b(dalam|di) ranah\b|\bholistik\b|\bsinergi\b|\btransformatif\b|\bmenavigasi\b|\bberesonansi\b"
     r"|\bmembuka potensi\b|\bbukti nyata\b|\bgame[- ]changer\b|\bpengubah permainan\b"
     r"|\b(ke )?level (berikutnya|selanjutnya)\b|\btanpa hambatan\b|\b(secara|dengan) mulus\b"
     r"|\byang terus berkembang\b|\bsegudang\b|\bmengungkap (rahasia|misteri)\b"
     r"|\bmemainkan peran(an)?\b|\bmemegang peran(an)? (yang )?(sangat )?(penting|krusial|vital|kunci)\b",
     "Pakai kata biasa (penting, membahas, di, memakai) atau sebut faktanya."),
    ("L5", KERAS, "kiasan puitis klise",
     r"\b(merajut|menenun|menyulam) (masa depan|asa|mimpi|kebersamaan|harapan|kisah|cerita|makna|kenangan)\b"
     r"|\bmenjelma (menjadi|sebagai)\b|\bsaksi bisu\b|\btak lekang oleh waktu\b|\bsurga tersembunyi\b"
     r"|\bmemanjakan (mata|lidah)\b|\bdenyut nadi\b|\bsimfoni\b",
     "Ganti kiasan dengan deskripsi konkret."),
    ("L5", KERAS, "jembatan pemasaran klise",
     r"\b(kini|telah|sudah) hadir\b|\bhadir (sebagai|untuk menjawab|menjawab|memberikan solusi)\b"
     r"|\bsolusi (terbaik|tepat|jitu|lengkap|terpercaya|tepercaya|praktis|cerdas|all-in-one)\b"
     r"|\b(tak|tidak|nggak|gak) perlu (pusing|khawatir|repot|bingung|ribet) lagi\b"
     r"|\bsiap menemani\b|\brasakan (perbedaannya|sensasinya|pengalaman)\b"
     r"|\bbayangkan (jika|kalau|betapa|bila)\b"
     r"|\bjangan (sampai )?(lewatkan|ketinggalan|terlewat|kelewatan)\b"
     r"|\bpengalaman (yang )?(tak|tidak) terlupakan\b|\bdirancang khusus untuk\b"
     r"|\bpilihan (tepat|cerdas|terbaik)\b|\bwajib (dicoba|diketahui|dikunjungi|punya|dimiliki)\b"
     r"|\bkualitas terbaik\b|\bdengan bangga (mengumumkan|mempersembahkan|menghadirkan|memperkenalkan)\b",
     "Sebut produk dan tindakannya langsung; ganti janji dengan fakta dari brief."),
    # ---- L7 kalimat meta dan kata pengisi
    ("L7", KERAS, "kalimat meta",
     r"\b(artikel|tulisan|panduan|pembahasan|makalah) ini akan (membahas|mengulas|menjelaskan|mengupas)\b"
     r"|\b(dalam|di|pada) (artikel|tulisan|pembahasan|kesempatan) (ini|kali ini),? "
     r"(kita|kami|saya|penulis|kamu|anda) akan\b"
     r"|\bmari (kita )?(simak|bahas|telusuri|kupas|lihat lebih)\b|\byuk,? (kita )?(simak|bahas|intip|kupas)\b"
     r"|\bsimak (ulasan|penjelasan|pembahasan|selengkapnya|sampai (habis|akhir|selesai))\b"
     r"|\btanpa berlama-lama\b|\bsebelum (membahas|masuk) lebih (lanjut|jauh|dalam)\b"
     r"|\bseperti yang (telah|sudah) (disebutkan|dijelaskan|dibahas)\b",
     "Hapus; langsung sampaikan isinya."),
    ("L7", KERAS, "kata pengisi",
     r"\b(perlu|penting) (untuk )?(diingat|diketahui|dicatat|diperhatikan|digarisbawahi|dipahami) bahwa\b"
     r"|\bpatut dicatat\b|\bdapat dikatakan bahwa\b|\bmerupakan hal yang (sangat )?penting\b"
     r"|\btidak dapat dipisahkan dari\b",
     "Hapus; kalimatnya tetap berdiri."),
    ("L7", TINJAU, "kata pengisi",
     r"\b(tentunya|pastinya|sejatinya|pada dasarnya|pada hakikatnya|secara keseluruhan|dalam hal ini)\b",
     "Biasanya bisa dihapus tanpa mengubah makna."),
    ("L7", TINJAU, "pertanyaan dijawab sendiri",
     r"(^|[.!?]\s+)(hasilnya|kabar baiknya|masalahnya|jawabannya|artinya|faktanya|intinya|solusinya)\?\s"
     r"|\b(mengapa|kenapa) (ini|hal ini|itu) penting\?",
     "Ubah jadi pernyataan."),
    ("L7", TINJAU, "pembuka bertahap",
     r"(^|[.!?]\s+)(faktanya,|jujur saja,|sejujurnya,|begini,|menariknya,|yang menarik(nya)?,?"
     r"|inilah (kuncinya|intinya)|nah, ini dia|pertanyaannya:|kabar (baiknya|gembira(nya)?)( lagi)?[:,!])",
     "Hapus pengantarnya; sampaikan isinya."),
    # ---- L8 kabur
    ("L8", KERAS, "atribusi kabur",
     r"\b(para|banyak|sejumlah|beberapa|sebagian) (ahli|pakar|peneliti|pengamat|orang)( \w+)? "
     r"(menilai|berpendapat|percaya|mengatakan|menyebut(kan)?|sepakat|meyakini)\b"
     r"|\b(sejumlah|banyak|beberapa|berbagai) (penelitian|studi|riset|survei|sumber) "
     r"(menunjukkan|membuktikan|menyebutkan|mengungkap(kan)?)\b"
     r"|\bmenurut (para ahli|para pakar|berbagai sumber)\b",
     "Sebut nama dan tahun, atau buang klaimnya."),
    ("L8", TINJAU, "lindung nilai bertumpuk",
     r"\b(mungkin|barangkali|bisa jadi|cenderung|relatif|agaknya)\b[^.!?\n]{0,25}"
     r"\b(mungkin|barangkali|bisa jadi|cenderung|relatif)\b",
     "Satu penanda ketidakpastian cukup."),
    # ---- L9 jejak asisten, menjilat, superlatif
    ("L9", KERAS, "jejak asisten",
     r"(^|\n)\s*(tentu|tentu saja|baik|baiklah)[!,]\s+(berikut|ini dia|saya akan)\b"
     r"|\bsemoga membantu\b|\bsebagai (sebuah )?(model bahasa|asisten ai)\b"
     r"|\b(apakah (anda|kamu) (ingin|mau)|mau|perlu) saya "
     r"(buatkan|bantu|tambahkan|sesuaikan|lanjutkan|perpendek|ubah)\b"
     r"|\bsaya (juga )?bisa (membuatkan|menambahkan|menyesuaikan|menyusun)\b"
     r"|\bjika (ada|anda memiliki|kamu punya) pertanyaan (lain|lebih lanjut)\b",
     "Serahkan teksnya saja, tanpa pengantar dan tanpa tawaran lanjutan."),
    ("L9", KERAS, "menjilat",
     r"\b(pertanyaan|ide|poin|pemikiran) yang (sangat )?(bagus|menarik|luar biasa|tepat)\b"
     r"|\b(anda|kamu) benar sekali\b",
     "Hapus; langsung jawab."),
    ("L9", TINJAU, "superlatif butuh bukti",
     r"\b(terbaik|termurah|terlengkap|tercepat|terdepan|terlaris|nomor satu"
     r"|no\. ?1|satu-satunya|revolusioner|dijamin)\b",
     "Sah hanya dengan bukti yang disebutkan (EPI butir 1.2.2); tanpa itu, ganti fakta."),
    # ---- L10 format dan jejak alat
    ("L10", KERAS, "jejak alat",
     r"oaicite|contentReference|turn\d+(search|view|news)\d+|utm_source=(chatgpt|openai|claude|gemini|copilot)"
     r"|【[^】\n]*】|\[cite: ?\d+\]",
     "Hapus; itu sisa keluaran mesin."),
    ("L10", KERAS, "templat belum diisi",
     r"\[(nama|tanggal|alamat|nomor|link|tautan|url|perusahaan|produk|merek|brand|kota|jabatan|judul|harga)"
     r"[^\]\n]{0,30}\](?!\()",
     "Isi dengan data nyata, atau tanyakan ke pengguna."),
    ("L10", KERAS, "tanda seru ganda", r"!{2,}", "Satu tanda seru sudah keras."),
    ("L10", KERAS, "hashtag generik",
     r"(?<!\w)#(fyp|foryou|foryoupage|viral|trending|xyzbca|fypシ)\b",
     "Pakai hashtag yang spesifik untuk isi unggahan."),
    # ---- EJ / TB
    ("EJ", KERAS, "kata depan dirangkai",
     r"\b(dimana|kemana|disini|disitu|disana|diantara|diatas|dibawah|didalam|diluar|disamping"
     r"|kedalam|keatas|kebawah|kesana|kesini)\b",
     "Kata depan di/ke ditulis terpisah: di mana, di sini, ke dalam."),
    ("EJ", KERAS, "gabungan kata",
     r"\b(terimakasih|tanggungjawab|kerjasama|orangtua|walikota|sosial media)\b",
     "terima kasih, tanggung jawab, kerja sama, orang tua, wali kota, media sosial."),
    ("TB", KERAS, "yang mana / di mana sebagai penghubung",
     r"\byang (di ?)?mana\b",
     "Pakai yang, tempat, saat, sehingga, atau pecah kalimatnya."),
    ("TB", TINJAU, "di mana sebagai penghubung",
     r"\b\w{3,},? di mana (pengguna|kita|kami|anda|kamu|mereka|ia|dia|setiap|semua|para|orang)\b",
     "Kalau bukan pertanyaan tentang tempat: pakai tempat, yang, saat."),
    ("TB", KERAS, "kopula ganda", r"\badalah merupakan\b|\bmerupakan adalah\b", "Pilih satu."),
    ("TB", TINJAU, "adalah + untuk", r"\badalah untuk\b", "'tujuannya adalah untuk X' menjadi 'tujuannya X'."),
    ("TB", KERAS, "pleonasme",
     r"\bagar supaya\b|\bdemi untuk\b|\bnaik ke atas\b|\bturun ke bawah\b|\bmundur ke belakang\b"
     r"|\bmaju ke depan\b|\bsejak dari\b|\bmulai sejak\b|\bdalam rangka untuk\b|\bdisebabkan karena\b"
     r"|\bseperti misalnya\b|\bpara hadirin\b|\bsangat \w+ sekali\b|\bsaling \w+-me\w+\b",
     "Buang salah satu."),
    ("TB", KERAS, "konjungsi ganda",
     r"\b(meskipun|walaupun|meski|walau)\b[^.!?\n]{3,100}?,\s*(tetapi|tapi|namun)\b"
     r"|\bkarena\b[^.!?\n]{3,100}?,\s*maka\b",
     "Satu konjungsi per hubungan."),
    ("TB", TINJAU, "subjek berkata depan",
     r"(^|[.!?]\s+)(bagi|kepada|dalam|dari|menurut|berdasarkan) [^.,!?\n]{3,60} "
     r"(menunjukkan|menyatakan|menyebutkan|membuktikan|mengatakan|memutuskan|dipersilakan)\b",
     "'Dalam laporan ini menunjukkan' menjadi 'Laporan ini menunjukkan'."),
    ("TB", TINJAU, "verba semu",
     r"\b(melakukan|memberikan|mengadakan) pe\w+an\b"
     r"|\bmengalami (peningkatan|penurunan|kenaikan)\b",
     "Verba tunggal lebih kuat: menganalisis, menjelaskan, naik."),
    ("TB", KERAS, "kalque",
     r"\b(pada|di) (akhir|penghujung) hari\b|\bmembuat (sebuah )?perbedaan\b"
     r"|\bsemoga (email|surel|pesan) ini menemukan\b",
     "Pakai ungkapan Indonesia yang wajar."),
]

ATURAN_TERKOMPILASI = [(k, t, n, re.compile(p, re.IGNORECASE), s) for k, t, n, p, s in ATURAN]

# Kata nonbaku -> baku. Rujukan akhir: KBBI Daring (kbbi.kemendikdasmen.go.id).
# Harus sama dengan references/kata-baku.md (diperiksa tests/test_periksa.py).
NONBAKU = {
    "silahkan": "silakan", "sekedar": "sekadar", "resiko": "risiko", "praktek": "praktik",
    "analisa": "analisis", "ijin": "izin", "aktifitas": "aktivitas", "ambulan": "ambulans",
    "handal": "andal", "antri": "antre", "apotik": "apotek", "azas": "asas", "asik": "asyik",
    "atlit": "atlet", "otentik": "autentik", "cabe": "cabai", "cinderamata": "cendera mata",
    "detil": "detail", "diagnosa": "diagnosis", "efektifitas": "efektivitas", "ekstrim": "ekstrem",
    "elit": "elite", "hembus": "embus", "esei": "esai", "pebruari": "Februari", "pondasi": "fondasi",
    "frekwensi": "frekuensi", "hapal": "hafal", "hipotesa": "hipotesis", "ijasah": "ijazah",
    "himbau": "imbau", "hisap": "isap", "isteri": "istri", "jadual": "jadwal", "kaedah": "kaidah",
    "karir": "karier", "katagori": "kategori", "kuatir": "khawatir", "kawatir": "khawatir",
    "komplit": "komplet", "komplek": "kompleks", "konkrit": "konkret", "konsekwensi": "konsekuensi",
    "kreatifitas": "kreativitas", "produktifitas": "produktivitas", "kwalitas": "kualitas",
    "kwitansi": "kuitansi", "lembab": "lembap", "mahluk": "makhluk", "materai": "meterai",
    "milyar": "miliar", "nahkoda": "nakhoda", "nafas": "napas", "nasehat": "nasihat",
    "nopember": "November", "nomer": "nomor", "obyek": "objek", "faham": "paham", "perduli": "peduli",
    "fikir": "pikir", "propinsi": "provinsi", "rapih": "rapi", "respon": "respons",
    "rejeki": "rezeki", "seksama": "saksama", "syaraf": "saraf", "sekertaris": "sekretaris",
    "sintesa": "sintesis", "supir": "sopir", "standard": "standar", "subyek": "subjek",
    "survey": "survei", "tehnik": "teknik", "terlanjur": "telanjur", "terlentang": "telentang",
    "tentram": "tenteram", "teoritis": "teoretis", "trampil": "terampil", "hutang": "utang",
    "jaman": "zaman", "terpercaya": "tepercaya", "sholat": "salat", "shalat": "salat",
    "ramadhan": "Ramadan", "adzan": "azan", "mushola": "musala", "musholla": "musala",
}
# Bentuk yang hanya salah sebagai kata utuh (tidak diberi imbuhan otomatis).
NONBAKU_UTUH = {
    "merubah": "mengubah", "dirubah": "diubah",
    "mempengaruhi": "memengaruhi", "mempesona": "memesona", "memerhatikan": "memperhatikan",
    "jum'at": "Jumat", "do'a": "doa",
}
# Hanya akar berikut yang dicocokkan bersama imbuhan (beresiko, mempraktekkan,
# ketrampilan). Akar lain dicocokkan sebagai kata utuh agar "penelitian" tidak
# terbaca sebagai pen-elit-i-an.
BERIMBUHAN = {
    "resiko", "praktek", "analisa", "ijin", "antri", "himbau", "hisap", "hembus", "nafas", "nasehat",
    "fikir", "faham", "hutang", "respon", "survey", "kuatir", "hapal", "perduli", "rapih", "trampil",
    "aktifitas", "silahkan", "handal",
}
_AWALAN = r"(?:me|mem|men|meng|di|be|ber|ter|pe|pem|pen|peng|per|se|ke|memper|diper)?"
_AKHIRAN = r"(?:kan|i|an|nya|lah|kah|ku|mu){0,2}"


def _gabung(kata):
    return "|".join(sorted(map(re.escape, kata), key=len, reverse=True))


RE_NONBAKU = re.compile(
    r"\b(?:" + _AWALAN + r"(" + _gabung(BERIMBUHAN) + r")" + _AKHIRAN
    + r"|(" + _gabung(set(NONBAKU) - BERIMBUHAN) + r")(?:nya)?)\b", re.IGNORECASE)
RE_NONBAKU_UTUH = re.compile(
    r"(?<![\w'])(" + "|".join(map(re.escape, NONBAKU_UTUH)) + r")(?:nya|kan|lah)?(?![\w'])", re.IGNORECASE)

KATA_SIFAT_IKLAN = set(
    "cepat mudah murah aman nyaman terpercaya tepercaya terjangkau praktis efektif efisien inovatif "
    "kreatif inspiratif andal handal modern elegan berkualitas profesional terbaik lengkap canggih "
    "hemat fleksibel akurat transparan ramah responsif tangguh stabil simpel sederhana gampang lancar "
    "berkelanjutan terintegrasi optimal unggul dinamis adaptif kolaboratif".split())
RE_TRIPEL = re.compile(r"\b(\w+), (\w+),? (?:dan|serta|&) (\w+)\b", re.IGNORECASE)

KATA_TUGAS = set(
    "dan atau yang di ke dari untuk dengan pada dalam bagi oleh tentang sebagai serta terhadap kepada "
    "karena agar supaya tetapi hingga sampai antara tanpa daripada".split())
RE_JUDUL = re.compile(r"^\s*(?:#{1,6}\s+|(?:judul|title|headline|subjudul|h[1-6])\s*:\s*)(.+)$", re.IGNORECASE)

TRANSISI = (
    "selain itu", "tidak hanya itu", "tak hanya itu", "terlebih lagi", "lebih lanjut", "lebih jauh",
    "tak kalah penting", "yang tidak kalah", "namun demikian", "oleh karena itu", "oleh sebab itu",
    "dengan demikian", "di sisi lain", "sementara itu", "adapun", "selanjutnya", "dalam hal ini",
    "pada akhirnya", "secara keseluruhan", "di samping itu", "maka dari itu", "dengan kata lain",
    "meski demikian", "meskipun demikian", "kendati demikian",
)
RE_TRANSISI = re.compile(r"^(" + "|".join(TRANSISI) + r")\b", re.IGNORECASE)

CAKAPAN = re.compile(
    r"\b(nggak|gak|ga|enggak|banget|gimana|kayak|bikin|doang|udah|aja|dong|sih|deh|nih|lho|yuk|kok)\b",
    re.IGNORECASE)
RE_EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B50\u2B06]")
RE_HASHTAG = re.compile(r"(?<![\w&])#(?!\d+\b)[A-Za-z0-9_]{2,}")
RE_PISAH = re.compile(r"—|(?<=\s)–(?=\s)|(?<=\w) -- (?=\w)")
RE_RENTANG = re.compile(r"(?<=\d)—(?=\d)|(?<=[A-Za-z])—(?=[A-Z])")
RE_KALIMAT = re.compile(r"(?<=[.!?…])[\"”')\]]*\s+")
RE_KUTIPAN = re.compile(r"[\"“][^\"”\n]*[\"”]")
RAGAM_FORMAL = ("beku", "resmi", "konsultatif")


def baris_bersih(teks):
    """Hasilkan (nomor, isi) tanpa frontmatter, blok kode, kode sebaris, dan URL."""
    baris = teks.splitlines()
    mulai = 0
    if baris and baris[0].strip() == "---":
        for i in range(1, len(baris)):
            if baris[i].strip() == "---":
                mulai = i + 1
                break
    dalam_kode = False
    for no in range(mulai, len(baris)):
        isi = baris[no]
        if isi.lstrip().startswith("```"):
            dalam_kode = not dalam_kode
            continue
        if dalam_kode:
            continue
        isi = re.sub(r"`[^`\n]*`", lambda m: " " * len(m.group()), isi)
        isi = re.sub(r"\]\([^)\n]*\)", lambda m: "]" + " " * (len(m.group()) - 1), isi)
        isi = re.sub(r"https?://\S+", lambda m: " " * len(m.group()), isi)
        yield no + 1, isi


def _tambah(temuan, kode, tingkat, nama, kutipan, saran, baris=0, kolom=0):
    temuan.append({"kode": kode, "tingkat": tingkat, "nama": nama, "kutipan": kutipan.strip()[:90],
                   "saran": saran, "baris": baris, "kolom": kolom})


def _buang_markup(isi):
    return re.sub(r"^\s*(>\s*)*([-*•]\s+|\d+[.)]\s+|#{1,6}\s+)?", "", isi)


def _teks_judul(baris, idx):
    """Kembalikan teks judul bila baris ke-idx adalah judul, selain itu None.

    Judul: baris markdown '#', baris berlabel 'Judul:', atau baris tunggal
    (diapit baris kosong) tanpa tanda baca akhir yang sebagian besar katanya
    berhuruf kapital.
    """
    isi = baris[idx][1]
    m = RE_JUDUL.match(isi)
    if m:
        return m.group(1)
    t = isi.strip()
    if not t or len(t) > 110 or t[-1] in ".!?:,;" or t[0] in "#>|-*•" or "#" in t or t[0].isdigit() and t[1:2] in ".)":
        return None
    sebelum = baris[idx - 1][1].strip() if idx > 0 else ""
    sesudah = baris[idx + 1][1].strip() if idx + 1 < len(baris) else ""
    if sebelum or sesudah:
        return None
    kata = [k for k in re.findall(r"[A-Za-zÀ-ÿ'-]+", t)]
    if len(kata) < 3:
        return None
    isi_kata = [k for k in kata if k.lower() not in KATA_TUGAS]
    if not isi_kata or sum(k[0].isupper() for k in isi_kata) / len(isi_kata) < 0.7:
        return None
    return t


def periksa(teks, ragam=None, seo=False):
    """Kembalikan (daftar temuan, statistik)."""
    temuan = []
    baris = list(baris_bersih(teks))
    formal = ragam in RAGAM_FORMAL

    sudah_cek_panjang = False
    for idx, (no, isi) in enumerate(baris):
        for kode, tingkat, nama, rx, saran in ATURAN_TERKOMPILASI:
            for m in rx.finditer(isi):
                _tambah(temuan, kode, tingkat, nama, m.group(), saran, no, m.start() + 1)

        for m in RE_NONBAKU.finditer(isi):
            akar = (m.group(1) or m.group(2)).lower()
            _tambah(temuan, "EJ", KERAS, "kata tidak baku", m.group(),
                    f"Bentuk baku: {NONBAKU[akar]} (cek KBBI bila ragu).", no, m.start() + 1)
        for m in RE_NONBAKU_UTUH.finditer(isi):
            _tambah(temuan, "EJ", KERAS, "kata tidak baku", m.group(),
                    f"Bentuk baku: {NONBAKU_UTUH[m.group(1).lower()]}.", no, m.start() + 1)
        for m in re.finditer(r"(?<![\w@./-])anda\b", isi):
            _tambah(temuan, "EJ", KERAS, "Anda tanpa kapital", m.group(),
                    "Anda selalu berhuruf kapital.", no, m.start() + 1)

        for m in RE_TRIPEL.finditer(isi):
            if sum(k.lower() in KATA_SIFAT_IKLAN for k in m.groups()) >= 2:
                _tambah(temuan, "L4", KERAS, "tripel kata sifat", m.group(),
                        "Pilih satu yang paling benar, atau ganti dengan bukti.", no, m.start() + 1)

        for m in RE_PISAH.finditer(isi):
            rentang = RE_RENTANG.match(isi, m.start()) is not None
            if rentang and not formal:
                _tambah(temuan, "L10", TINJAU, "tanda pisah untuk rentang", isi[max(0, m.start() - 8):m.end() + 8],
                        "Sah menurut EYD V; paket ini menyarankan 'sampai'.", no, m.start() + 1)
            else:
                _tambah(temuan, "L10", KERAS, "tanda pisah sebagai tanda baca gaya",
                        isi[max(0, m.start() - 12):m.end() + 12],
                        "Ganti koma, titik, atau kurung; rentang ditulis 'sampai'.", no, m.start() + 1)

        sisa = _buang_markup(isi)
        if len(sisa) > 3 and RE_EMOJI.match(sisa):
            _tambah(temuan, "L10", TINJAU, "emoji membuka baris", sisa[:30],
                    "Emoji sebagai butir daftar atau hiasan judul: buang, kecuali penanda genre.", no, 1)

        judul = _teks_judul(baris, idx)
        if judul and not judul.isupper():
            if seo and not sudah_cek_panjang:
                sudah_cek_panjang = True
                if len(judul.strip()) > 60:
                    _tambah(temuan, "L10", TINJAU, "judul lebih dari 60 karakter", f"{len(judul.strip())} karakter",
                            "Sebagai title tag akan terpotong di hasil pencarian; patokan 50 sampai 60.", no, 1)
            kata = re.findall(r"[A-Za-zÀ-ÿ0-9'/%-]+|[:?!]", judul)
            for i, k in enumerate(kata[1:], 1):
                if k[0].isupper() and k.lower() in KATA_TUGAS and kata[i - 1] not in ":?!":
                    _tambah(temuan, "L10", KERAS, "kata tugas berhuruf kapital di judul", k,
                            "EYD V: kata tugas (dan, di, untuk, yang, ...) huruf kecil kecuali di awal judul.",
                            no, isi.find(k) + 1)

        if formal:
            for m in CAKAPAN.finditer(isi):
                _tambah(temuan, "KS", TINJAU, "kata percakapan di ragam formal", m.group(),
                        "Sesuaikan dengan ragam, kecuali di dalam kutipan.", no, m.start() + 1)

    # ---------- pemeriksaan seluruh teks
    isi_semua = "\n".join(isi for _, isi in baris)
    kata = re.findall(r"[A-Za-zÀ-ÿ0-9'-]+", isi_semua)
    n_kata = len(kata)

    tagar = RE_HASHTAG.findall(isi_semua)
    if len(tagar) > 5:
        _tambah(temuan, "L10", KERAS, "hashtag berlebih", f"{len(tagar)} hashtag",
                "Maksimal 5 (batas Instagram dan TikTok); pilih 3 sampai 5 yang spesifik.")
    n_emoji = len(RE_EMOJI.findall(isi_semua))
    if n_emoji > 3 and "❌" not in isi_semua and "✅" not in isi_semua:
        _tambah(temuan, "L10", TINJAU, "emoji banyak", f"{n_emoji} emoji",
                "Maksimal 2 sampai 3 per caption, hanya bila menambah nada.")
    n_garis = len(re.findall(r"(?m)^\s*(-{3,}|\*{3,}|_{3,})\s*$", isi_semua))
    if n_garis >= 2:
        _tambah(temuan, "L10", TINJAU, "garis pemisah antarbagian", f"{n_garis} garis",
                "Buang kecuali format medium menuntutnya.")
    n_label = len(re.findall(r"(?m)^\s*(?:[-*•]|\d+[.)])\s+\*\*[^*\n]+\*\*\s*:|^\s*(?:[-*•]|\d+[.)])\s+\*\*[^*\n]+:\*\*",
                             isi_semua))
    if n_label >= 3:
        _tambah(temuan, "L10", TINJAU, "butir berlabel tebal berulang", f"{n_label} butir",
                "Pola 'label tebal: penjelasan' beruntun: tulis sebagai prosa atau daftar biasa.")
    n_judul = len(re.findall(r"(?m)^#{1,6}\s", isi_semua))
    if n_judul >= 2 and n_kata < 300:
        _tambah(temuan, "L10", TINJAU, "subjudul pada teks pendek", f"{n_judul} judul, {n_kata} kata",
                "Teks di bawah 300 kata umumnya cukup prosa.")
    if re.search(r"[“”]", isi_semua) and '"' in isi_semua:
        _tambah(temuan, "L10", TINJAU, "tanda petik campur", "kutip lurus dan keriting",
                "Seragamkan satu gaya.")

    # paragraf dan transisi
    paragraf = [p.strip() for p in re.split(r"\n\s*\n", isi_semua) if p.strip()]
    bersih = [_buang_markup(p.splitlines()[0]) for p in paragraf]
    for i in range(1, len(bersih)):
        a, b = RE_TRANSISI.match(bersih[i - 1]), RE_TRANSISI.match(bersih[i])
        if a and b:
            _tambah(temuan, "L6", KERAS, "dua paragraf beruntun dibuka transisi",
                    f"{a.group()} … / {b.group()} …", "Sambungkan lewat isi; buang salah satu transisi.")
    hitung = {}
    for t in TRANSISI:
        n = len(re.findall(r"\b" + re.escape(t) + r"\b", isi_semua, re.IGNORECASE))
        if n:
            hitung[t] = n
    for t, n in hitung.items():
        if n >= 2 and n > max(1, n_kata // 400):
            _tambah(temuan, "L6", TINJAU, "transisi berulang", f"'{t}' {n} kali dalam {n_kata} kata",
                    "Pakai sekali, atau biarkan urutan isi yang menyambung.")

    # sapaan dan kata ganti
    tanpa_kutipan = RE_KUTIPAN.sub(" ", isi_semua)
    kedua = {"Anda": len(re.findall(r"\banda\b", tanpa_kutipan, re.IGNORECASE)),
             "kamu": len(re.findall(r"\bkamu\b", tanpa_kutipan, re.IGNORECASE)),
             "lo": len(re.findall(r"\b(lo|lu|elo)\b", tanpa_kutipan))}
    dipakai = {k: v for k, v in kedua.items() if v}
    if len(dipakai) > 1:
        _tambah(temuan, "KS", KERAS, "sapaan tercampur", ", ".join(f"{k} ({v})" for k, v in dipakai.items()),
                "Satu teks satu sapaan.")
    pertama = {"saya": len(re.findall(r"\bsaya\b", tanpa_kutipan, re.IGNORECASE)),
               "aku": len(re.findall(r"\baku\b", tanpa_kutipan, re.IGNORECASE)),
               "gue": len(re.findall(r"\b(gue|gw|gua)\b", tanpa_kutipan, re.IGNORECASE))}
    dipakai = {k: v for k, v in pertama.items() if v}
    if len(dipakai) > 1:
        _tambah(temuan, "KS", TINJAU, "kata ganti orang pertama tercampur",
                ", ".join(f"{k} ({v})" for k, v in dipakai.items()), "Seragamkan sesuai ragam.")

    # rujukan kabur
    n_hal = len(re.findall(r"\b(hal ini|hal tersebut|tersebut)\b", isi_semua, re.IGNORECASE))
    if n_hal >= 3 and n_hal * 100 > n_kata:
        _tambah(temuan, "TB", TINJAU, "'hal ini/tersebut' berulang", f"{n_hal} kali dalam {n_kata} kata",
                "Sebut bendanya langsung, atau gabungkan kalimatnya.")

    # ritme dan pola pengganti
    prosa = [_buang_markup(isi) for _, isi in baris
             if isi.strip() and not isi.lstrip().startswith(("#", "|"))]
    kalimat = [k for p in prosa for k in RE_KALIMAT.split(p) if len(re.findall(r"\w+", k)) >= 1]
    panjang = [len(re.findall(r"[A-Za-zÀ-ÿ0-9'-]+", k)) for k in kalimat]
    if len(panjang) >= 6:
        rata = statistics.mean(panjang)
        simpang = statistics.pstdev(panjang)
        if rata >= 10 and simpang / rata < 0.28:
            _tambah(temuan, "PG", TINJAU, "panjang kalimat seragam",
                    f"rata-rata {rata:.0f} kata, simpangan {simpang:.1f}",
                    "Selingi kalimat pendek; gabung atau pecah beberapa kalimat.")
    runtun = 0
    for p in panjang:
        runtun = runtun + 1 if p <= 3 else 0
        if runtun == 3:
            _tambah(temuan, "PG", TINJAU, "kalimat sangat pendek beruntun", "3 kalimat ≤3 kata berturut-turut",
                    "Dramatisasi staccato adalah pengganti slop lama; gabungkan.")
            break
    teks_prosa = "\n".join(prosa)
    n_titik_dua = len(re.findall(r"(?<=[a-zà-ÿ]): (?=\S)", teks_prosa))
    if n_titik_dua >= 3 and n_titik_dua * 60 > n_kata:
        _tambah(temuan, "PG", TINJAU, "titik dua bertubi", f"{n_titik_dua} kali dalam {n_kata} kata",
                "Titik dua pembuka rincian wajar; titik dua 'pengumuman' yang berulang diganti kalimat biasa.")
    n_titik_koma = teks_prosa.count(";")
    if n_titik_koma >= 3 and n_titik_koma * 100 > n_kata:
        _tambah(temuan, "PG", TINJAU, "titik koma bertubi", f"{n_titik_koma} kali dalam {n_kata} kata",
                "Pecah jadi kalimat terpisah.")
    n_bukan = len(re.findall(r", bukan\b|\balih-alih\b|\bketimbang\b", teks_prosa, re.IGNORECASE))
    if n_bukan >= 3 and n_bukan * 120 > n_kata:
        _tambah(temuan, "PG", TINJAU, "kontras 'X, bukan Y' berulang", f"{n_bukan} kali dalam {n_kata} kata",
                "Bentuk terbalik paralelisme negatif; nyatakan X saja bila Y tak pernah diduga pembaca.")

    temuan.sort(key=lambda t: (t["baris"] == 0, t["baris"], t["kolom"]))
    statistik = {"kata": n_kata, "kalimat": len(panjang),
                 "keras": sum(t["tingkat"] == KERAS for t in temuan),
                 "tinjau": sum(t["tingkat"] == TINJAU for t in temuan)}
    return temuan, statistik


def cetak(sumber, temuan, st):
    print(f"== {sumber}: {st['kata']} kata, {st['kalimat']} kalimat | KERAS {st['keras']}, TINJAU {st['tinjau']}")
    for t in temuan:
        letak = f"{t['baris']}:{t['kolom']}" if t["baris"] else "teks"
        print(f"  {letak:>8}  {t['tingkat']:<6} [{t['kode']}] {t['nama']}: \"{t['kutipan']}\"\n"
              f"            -> {t['saran']}")
    if not temuan:
        print("  Tidak ada pola yang dikenali.")
    print("  Catatan: spesifisitas, dasar klaim, dan ketepatan ragam tidak bisa diperiksa skrip; baca ulang.")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Pemeriksa slop dan salah tulis bahasa Indonesia.")
    ap.add_argument("berkas", nargs="+", help="path berkas, atau - untuk stdin")
    ap.add_argument("--ragam", choices=["beku", "resmi", "konsultatif", "santai", "akrab"],
                    help="ragam teks; ragam formal memperketat tanda pisah dan kata percakapan")
    ap.add_argument("--seo", action="store_true", help="periksa juga panjang judul pertama (patokan title tag 60 karakter)")
    ap.add_argument("--json", action="store_true", help="keluaran JSON")
    ap.add_argument("--keras-saja", action="store_true", help="sembunyikan temuan TINJAU")
    ap.add_argument("--ketat", action="store_true", help="kode keluar 1 bila ada temuan KERAS")
    args = ap.parse_args(argv)

    hasil, ada_keras = [], False
    for path in args.berkas:
        if path == "-":
            teks = sys.stdin.read()
        else:
            with open(path, encoding="utf-8") as f:
                teks = f.read()
        temuan, st = periksa(teks, args.ragam, args.seo)
        if args.keras_saja:
            temuan = [t for t in temuan if t["tingkat"] == KERAS]
        ada_keras = ada_keras or st["keras"] > 0
        hasil.append({"berkas": path, "statistik": st, "temuan": temuan})

    if args.json:
        json.dump(hasil, sys.stdout, ensure_ascii=False, indent=2)
        print()
    else:
        for h in hasil:
            cetak(h["berkas"], h["temuan"], h["statistik"])
    return 1 if (args.ketat and ada_keras) else 0


if __name__ == "__main__":
    sys.exit(main())
