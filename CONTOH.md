# Contoh penggunaan: tanpa dan dengan bahasa-skills

Enam belas percobaan dijalankan pada 2 Agustus 2026 lewat subagent Claude Code: prompt pengguna yang sama persis dikerjakan tanpa dan dengan skill (untuk prompt contoh 1, dua model juga diuji kondisi pembanding "instruksi generik"), lalu setiap keluaran diperiksa terhadap Pemeriksaan Wajib [bahasa-inti](skills/bahasa-inti/SKILL.md) plus pemeriksaan tambahan kategorinya. Dokumen ini memuat keluaran mentahnya, temuan pemeriksaannya, dan perbandingan lintas model.

| Kondisi | Instruksi yang diterima model |
|---|---|
| **Tanpa skill** | Prompt pengguna apa adanya; model dilarang membaca berkas apa pun. |
| **Instruksi generik** | Prompt pengguna plus satu kalimat "tulis senatural mungkin, hindari klise dan pola kalimat yang terasa seperti tulisan AI"; tanpa akses berkas. |
| **Dengan skill** | Model membaca SKILL.md pemandu, bahasa-inti, skill kategori yang cocok, dan references yang relevan, lalu menjalankan protokol penuh sampai Pemeriksaan Wajib. |

Kutipan pada blok ❌ ditampilkan apa adanya, termasuk em dash, emoji berlebih, dan klaim karangannya: semua itu bagian dari bukti. Kode L1 sampai L10 merujuk Sepuluh Larangan Keras di bahasa-inti. Merek "Kasirin" fiktif, dibuat untuk pengujian; data pada prompt contoh 2 dan 4 disediakan sebagai bahan uji.

## Contoh 1: caption Instagram (bahasa-marketing)

Prompt:

> Buatkan caption Instagram untuk akun @kasirin.id, aplikasi kasir untuk UMKM. Isinya pengumuman fitur baru: Kasirin sekarang bisa menerima pembayaran QRIS, gratis biaya transaksi sampai 31 Oktober 2026. Target pembaca: pemilik warung, kedai kopi, dan toko kelontong. Nada santai, sapaan 'kamu'.

### ❌ Tanpa skill (Sonnet 5)

> Buat kamu pemilik warung, kedai kopi, sampai toko kelontong—ini kabar yang kamu tunggu-tunggu 👀
>
> Kasirin sekarang resmi bisa terima pembayaran QRIS!
>
> Pelanggan tinggal scan, bayar, selesai. Nggak perlu lagi bilang "maaf ya, di sini cuma cash" ke pembeli yang dompetnya isinya kartu semua.
>
> Dan yang bikin makin enak: biaya transaksi GRATIS sampai 31 Oktober 2026. Semua uang dari QRIS masuk utuh ke usaha kamu, nggak ada potongan.
>
> Dari racik kopi pagi-pagi sampai belanja bulanan di toko kelontong, sekarang semua jenis pembayaran bisa kamu handle cuma dari satu aplikasi kasir.
>
> Yuk, aktifkan QRIS di Kasirin kamu sekarang, mumpung masih gratis biaya transaksinya. Usaha lancar, transaksi gampang, cuan tetap utuh 💸
>
> `#Kasirin #KasirinID #AplikasiKasir #QRIS #UMKM #WarungNaikKelas #KedaiKopi #TokoKelontong #UsahaDigital`

Temuan (5):

1. Em dash sebagai tanda baca gaya di baris pertama ("kelontong—ini kabar") → L10.
2. Penutup tripel "Usaha lancar, transaksi gampang, cuan tetap utuh" → L4.
3. Sembilan hashtag, sebagian generik → melanggar batas 3 sampai 5 hashtag spesifik milik bahasa-marketing.
4. "Semua jenis pembayaran bisa kamu handle" → klaim melebihi brief (yang baru hanya QRIS) plus campur kode tanpa perlu.
5. Hook "ini kabar yang kamu tunggu-tunggu" bisa menempel pada pengumuman apa pun → gagal uji spesifisitas.

### ✅ Dengan skill (Sonnet 5)

Empat keputusan awal yang dicatat model sebelum menulis: pembaca pemilik warung, kedai kopi, dan toko kelontong yang sudah kenal produk; ragam santai bersapaan "kamu"; medium caption Instagram dengan hook di ±125 karakter awal; satu pesan (QRIS kini ada, gratis biaya sampai 31 Oktober 2026). Asumsinya juga tercatat: QRIS terintegrasi di aplikasi tanpa alat tambahan, sehingga CTA mengarah ke aktivasi dalam aplikasi, bukan tautan unduh yang tidak disebut brief.

> Ada pembeli di warungmu pegang HP, bukan dompet. "Bisa bayar QRIS?" Kamu jawab apa?
>
> Sekarang jawabannya gampang: bisa.
> Kasirin sekarang terima pembayaran QRIS, langsung dari aplikasi yang biasa kamu pakai buat catat transaksi. Nggak perlu mesin tambahan, nggak perlu pasang aplikasi lain.
>
> Biaya transaksinya gratis sampai 31 Oktober 2026: uang dari tiap transaksi QRIS masuk utuh ke kamu, nggak kepotong sepeser pun.
>
> Buka aplikasi Kasirin, lalu aktifkan QRIS di menu pembayaran sekarang.
>
> `#kasirin #umkmnaikkelas #qriswarung #kasiraplikasi`

Temuan: nol pada pemeriksaan saya. Hook 83 karakter (muat sebelum potongan "…more"), sapaan tunggal, satu CTA, klaim berjangkar pada tenggat yang memang ada di brief, empat hashtag, tanpa emoji, tanpa em dash.

## Contoh 2: judul dan pembuka artikel (bahasa-seo)

Prompt:

> Tulis judul artikel dan paragraf pembuka (3-4 kalimat) untuk artikel blog yang menyasar kata kunci 'cara mengatur keuangan rumah tangga'. Konteks: blog edukasi keuangan untuk keluarga muda dengan penghasilan sekitar UMR, sapaan 'kamu'. Data yang boleh dipakai: aturan alokasi 50/30/20.

### ❌ Tanpa skill (Sonnet 5)

> Cara Mengatur Keuangan Rumah Tangga dengan Gaji UMR Pakai Rumus 50/30/20
>
> Gaji baru cair, tapi belum juga tanggal 25 saldo sudah menipis lagi — rasanya nggak asing, kan? Kalau kamu dan pasangan baru membangun rumah tangga dengan penghasilan di kisaran UMR, masalahnya biasanya bukan soal kurang usaha, melainkan belum ada pembagian yang jelas: mana jatah kebutuhan pokok, mana jatah keinginan, dan mana yang harus disisihkan lebih dulu sebelum kepakai buat hal lain. Salah satu cara paling gampang diterapkan adalah rumus 50/30/20, yaitu membagi penghasilan bulanan jadi tiga pos: 50% untuk kebutuhan, 30% untuk keinginan, dan 20% untuk tabungan sekaligus cicilan utang. Di artikel ini, kamu akan lihat cara menerapkan rumus itu ke kondisi rumah tangga sendiri, lengkap dengan contoh perhitungan biar nggak berhenti di teori doang.

Temuan (5):

1. Judul Title Case, tiap kata kapital → L10.
2. Judul 72 karakter → melampaui batas 50 sampai 60 karakter title tag.
3. Em dash di kalimat pertama ("menipis lagi — rasanya") → L10.
4. "Bukan soal kurang usaha, melainkan belum ada pembagian yang jelas" → paralelisme negatif, L3.
5. "Di artikel ini, kamu akan lihat…" → kalimat meta, L7; pembuka jadi janji, bukan jawaban, sehingga gagal uji featured snippet.

### ✅ Dengan skill (Sonnet 5)

Asumsi yang dicatat model: Rp3 juta dipakai sebagai contoh kondisional, bukan klaim besaran UMR, karena UMR berbeda tiap daerah dan datanya tidak diberikan.

> Cara mengatur keuangan rumah tangga gaji UMR: rumus 50/30/20
>
> Cara mengatur keuangan rumah tangga yang paling gampang dipraktikkan adalah rumus 50/30/20: separuh gaji untuk kebutuhan pokok, 30 persen untuk keinginan, dan 20 persen untuk tabungan atau cicilan. Kalau gajimu sekitar UMR, misalnya Rp3 juta sebulan, jatahnya kira-kira Rp1,5 juta untuk kebutuhan, Rp900 ribu untuk keinginan, dan Rp600 ribu untuk tabungan. Masalahnya, pembagian rapi ini sering berantakan begitu tanggal tua datang, ada cicilan motor, atau tiba-tiba diundang kondangan. Berikut cara menyesuaikan tiga pos itu supaya gajimu cukup sampai akhir bulan.

Temuan: nol. Judul 60 karakter persis, kata kunci di depan, huruf kapital hanya di kata pertama. Kalimat pertama langsung menjawab kueri (layak featured snippet), contoh angkanya konsisten secara aritmetika, dan pembagian perannya jelas: judul menjanjikan, pembuka membuktikan.

## Contoh 3: pesan error aplikasi (bahasa-website)

Prompt:

> Tulis pesan error (judul, isi, dan label tombol) untuk aplikasi fintech saat pengguna gagal mengunggah foto KTP karena ukuran file melebihi 5 MB. Sapaan 'kamu', nada tenang dan membantu.

### ❌ Tanpa skill (Sonnet 5)

> Judul: Foto KTP Terlalu Besar
>
> Isi: Ukuran foto yang kamu unggah lebih dari 5 MB. Coba kompres atau ambil ulang fotonya dengan resolusi lebih kecil, lalu unggah lagi, ya.
>
> Label Tombol: Unggah Ulang

Temuan (2): judul dan tombol memakai Title Case ("Terlalu Besar", "Unggah Ulang"), padahal konvensi antarmuka memakai gaya kalimat. Isinya sendiri sudah memenuhi pola sebab plus solusi; ini contoh bagus bahwa keluaran tanpa skill tidak selalu hancur, yang hilang adalah konsistensi konvensi.

### ✅ Dengan skill (Sonnet 5)

Model mencatat satu keputusan yang menarik: default sapaan produk finansial di skill ini "Anda", tetapi prompt meminta "kamu", jadi permintaan pengguna yang menang dan penyimpangannya didokumentasikan.

> Judul: Foto KTP kelebihan ukuran
>
> Isi: Maksimal 5 MB, tapi foto yang kamu unggah masih lebih besar. Kompres dulu, atau gunakan foto dengan resolusi lebih kecil.
>
> Tombol: Pilih foto lain

Temuan: nol. Gaya kalimat konsisten, batasnya disebut, dua jalan keluar ditawarkan, tombol menyebut aksi berikutnya.

## Contoh 4: latar belakang skripsi (bahasa-peneliti)

Prompt:

> Tulis satu paragraf latar belakang (4-6 kalimat) untuk proposal skripsi tentang pengaruh intensitas penggunaan media sosial terhadap kesehatan mental remaja di Indonesia. Ragam resmi. Data yang tersedia dan boleh dipakai hanya ini: survei APJII 2024 mencatat penetrasi internet Indonesia 79,5%; laporan We Are Social Januari 2025 mencatat rata-rata pemakaian media sosial orang Indonesia 3 jam 11 menit per hari.

### ❌ Tanpa skill (Sonnet 5)

> Perkembangan teknologi digital telah mengubah secara mendasar pola komunikasi dan interaksi sosial masyarakat Indonesia, sebagaimana tercermin dari tingkat penetrasi internet yang telah mencapai 79,5% menurut survei Asosiasi Penyelenggara Jasa Internet Indonesia (APJII) tahun 2024. Kondisi ini sejalan dengan tingginya intensitas penggunaan media sosial di kalangan masyarakat Indonesia, yang menurut laporan We Are Social edisi Januari 2025 rata-rata mencapai 3 jam 11 menit per hari. Remaja merupakan salah satu kelompok pengguna yang paling intensif berinteraksi dengan platform tersebut karena tumbuh dan berkembang bersamaan dengan pesatnya kemajuan teknologi digital. Tingginya durasi keterpaparan pada media sosial ini menimbulkan kekhawatiran terhadap dampaknya bagi kondisi psikologis remaja, mengingat masa remaja merupakan tahap perkembangan yang krusial bagi pembentukan identitas diri dan kestabilan emosi. Hingga kini, kajian yang secara khusus mengungkap keterkaitan antara intensitas penggunaan media sosial dan kesehatan mental remaja di Indonesia masih perlu terus dikembangkan agar dapat memberikan gambaran yang lebih komprehensif. Berdasarkan uraian tersebut, penelitian ini dilakukan untuk mengkaji pengaruh intensitas penggunaan media sosial terhadap kesehatan mental remaja di Indonesia.

Temuan (5):

1. Pembuka kosmos "Perkembangan teknologi digital telah mengubah…" → slop akademik klasik yang dilarang eksplisit di bahasa-peneliti (keluarga L1).
2. "Krusial" → kosakata slop, L5.
3. "Kelompok pengguna yang paling intensif" → klaim peringkat tanpa data (data yang diizinkan tidak menyebut remaja paling intensif) → L8.
4. "Masih perlu terus dikembangkan agar dapat memberikan gambaran yang lebih komprehensif" → celah riset yang kabur, tanpa isi.
5. Kalimat pertama 33 kata beranak-cucu; enam kalimat nyaris seragam panjangnya → melanggar kaidah kalimat efektif akademik.

### ✅ Dengan skill (Sonnet 5)

> Survei Asosiasi Penyelenggara Jasa Internet Indonesia (APJII) tahun 2024 mencatat penetrasi internet nasional mencapai 79,5%. Laporan We Are Social edisi Januari 2025 turut mencatat rata-rata pengguna di Indonesia, termasuk remaja, mengakses media sosial selama 3 jam 11 menit per hari. Durasi tersebut bersinggungan langsung dengan waktu tidur, waktu belajar, dan waktu interaksi tatap muka remaja. Sejauh mana intensitas penggunaan tersebut memengaruhi kesehatan mental mereka masih perlu dikaji secara khusus dalam konteks Indonesia. Penelitian ini bertujuan menguji pengaruh intensitas penggunaan media sosial terhadap kesehatan mental remaja di Indonesia.

Temuan: nol. Kalimat pertama langsung data, struktur mengikuti pola fenomena berdata lalu celah lalu tujuan, kata ganti memakai konvensi "penelitian ini", dan tidak ada satu pun rujukan yang dikarang di luar dua data yang diberikan. Model bahkan melaporkan memperbaiki keparalelan rinciannya sendiri saat pemeriksaan.

## Perbandingan lintas model dan kondisi (prompt contoh 1)

Sepuluh percobaan dengan prompt caption yang sama. "Temuan" adalah jumlah pelanggaran hasil pemeriksaan manual; token dan durasi diambil dari usage subagent masing-masing.

| Model | Kondisi | Temuan | Yang paling mencolok | Token | Durasi |
|---|---|---|---|---|---|
| Haiku 4.5 | Tanpa skill | 6 | 4 emoji hias, 8 hashtag, CTA kabur "nikmatin kemudahannya", klaim tanpa jangkar, "Win-win!" | 30.198 | 6 dtk |
| Haiku 4.5 | Dengan skill | 2 | Tahun tenggat hilang ("sampai 31 Oktober" saja); "Caranya simple" | 57.376 | 79 dtk |
| Sonnet 5 | Tanpa skill | 5 | Em dash, tripel penutup, 9 hashtag, klaim melebihi brief | 44.203 | 22 dtk |
| Sonnet 5 | Instruksi generik | 2 | Em dash tetap lolos; dua CTA (aktifkan + cek bio) | 52.361 | 118 dtk |
| Sonnet 5 | Dengan skill | 0 | Asumsi integrasi dicatat eksplisit | 100.865 | 376 dtk |
| Opus 5 | Tanpa skill | 7 | Em dash ×2, 10 hashtag, dua CTA, fakta karangan "nggak pakai biaya pendaftaran", bold markdown di caption | 37.127 | 13 dtk |
| Opus 5 | Dengan skill | 0 | Memakai "pindai" sesuai daftar padanan | 77.860 | 160 dtk |
| Fable 5 | Tanpa skill | 1 | Angka karangan "nggak sampai lima menit" | 40.589 | 55 dtk |
| Fable 5 | Instruksi generik | 1 | Klaim kecepatan terselubung "kelar sebelum gorengan habis"; asumsi tak tercatat | 41.387 | 70 dtk |
| Fable 5 | Dengan skill | 0 | Melaporkan membuang sendiri klaim durasi karangan saat pemeriksaan | 78.767 | 263 dtk |

Empat bacaan dari tabel ini:

1. **Skill menyamakan hasil lintas kelas model.** Haiku dengan skill (2 temuan kecil) mengalahkan Opus tanpa skill (7 temuan). Aturan tertulis lebih menentukan daripada ukuran model.
2. **Model makin pintar, slop gayanya makin halus, tetapi kejujurannya belum otomatis.** Keluaran Fable tanpa skill sudah bersih dari klise, lalu tetap mengarang "nggak sampai lima menit" yang tidak ada di brief. Versi dengan skill membuang klaim itu dan mencatat asumsinya; larangan mengarang bukti memang aturan eksplisit bahasa-marketing.
3. **Instruksi generik "hindari gaya AI" menolong, tetapi tidak menggantikan daftar.** Sonnet masih meloloskan em dash karena "hindari klise" tidak memberi tahu penanda mana yang harus dicari; daftar frasa terlarang, batas hashtag, dan kewajiban mencatat asumsi adalah pengetahuan spesifik, bukan niat baik.
4. **Biayanya nyata: kondisi dengan skill memakan kira-kira dua kali token dan jauh lebih lama** karena model membaca empat sampai enam berkas lalu menjalankan pemeriksaan. Untuk banyak teks pendek dalam satu sesi, muat skillnya sekali di awal; berkas yang sudah berada di konteks tidak perlu dibaca ulang.

Satu catatan tambahan: enam dari sepuluh keluaran memakai hook percakapan "Bisa QRIS?" tanpa saling melihat. Ide pembuka model memang cenderung konvergen; yang dibedakan skill bukan idenya, melainkan disiplin klaim, format, dan pemeriksaannya.

## Empat kategori dengan model yang sama (Sonnet 5)

| Contoh | Kategori | Temuan tanpa skill | Temuan dengan skill | Selisih paling terasa |
|---|---|---|---|---|
| 1. Caption Instagram | marketing | 5 | 0 | Em dash dan tripel hilang; hashtag 9 jadi 4; klaim dipagari brief |
| 2. Judul + pembuka artikel | seo | 5 | 0 | Judul Title Case 72 karakter jadi kalimat 60 karakter; pembuka janji jadi jawaban |
| 3. Pesan error | website | 2 | 0 | Konvensi kapitalisasi antarmuka; penyimpangan sapaan didokumentasikan |
| 4. Latar belakang skripsi | peneliti | 5 | 0 | Pembuka kosmos jadi data di kalimat pertama; "krusial" dan celah kabur hilang |

Pesan error menunjukkan batas bawahnya: untuk teks 30 kata, model tanpa skill sudah dekat dengan benar, dan nilai skill tinggal di konsistensi konvensi. Makin panjang dan makin bebas formatnya (artikel, latar belakang), makin lebar jurangnya.

## Mengulang percobaan

Kalau paket terpasang sebagai plugin (lihat [README](README.md#instalasi)), skill terpicu sendiri dari description-nya dan pembungkus di bawah tidak diperlukan. Percobaan di dokumen ini memakai pembungkus eksplisit karena dijalankan lewat subagent tanpa plugin terpasang:

```text
Kamu akan mengerjakan satu tugas menulis memakai paket skill "bahasa-skills" yang ada di repo ini.

Langkah wajib, urut:
1. Baca SKILL.md di root repo (pemandu arah paket).
2. Ikuti arahannya: baca skills/bahasa-inti/SKILL.md, lalu SKILL.md kategori yang cocok,
   lalu berkas references/ yang relevan (minimal frasa-terlarang.md).
3. Kerjakan permintaan pengguna mengikuti seluruh protokol skill, lalu jalankan
   Pemeriksaan Wajib bahasa-inti plus pemeriksaan tambahan kategori sampai lolos semua.

Permintaan pengguna:
"<prompt>"
```

## Metode dan batasan

- Model yang diuji: `claude-haiku-4-5`, `claude-sonnet-5`, `claude-opus-5`, `claude-fable-5`; semuanya subagent Claude Code dengan pengaturan thinking bawaan sesi. Thinking tidak divariasikan per agen karena tidak bisa dikontrol dari pemanggilan subagent; yang divariasikan adalah model dan kondisi instruksi.
- Satu percobaan per sel, bukan rata-rata beberapa run, jadi angka temuan, token, dan durasi indikatif, bukan benchmark.
- Penilaian pelanggaran dilakukan manual terhadap Pemeriksaan Wajib bahasa-inti dan pemeriksaan tambahan kategori. Penilaian jenis ini punya wilayah abu-abu; hitungan di sini memakai tafsir yang sama untuk semua keluaran.
- Angka pada prompt (APJII 2024, We Are Social Januari 2025, aturan 50/30/20) disediakan sebagai bahan uji perilaku sitasi; verifikasi angkanya tetap tanggung jawab pemakai.
- Keluaran kondisi dengan skill dari Haiku sempat menyertakan teks proses di luar format yang diminta; yang dinilai hanya teks finalnya.
