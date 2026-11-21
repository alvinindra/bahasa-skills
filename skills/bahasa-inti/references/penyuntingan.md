# Menyunting dan Memeriksa Teks yang Sudah Ada

Dipakai ketika pengguna menyerahkan teks jadi: "perbaiki tulisan ini", "bikin lebih natural", "biar nggak kayak AI", "cek tulisan ini".

## Tentukan modenya

| Permintaan | Mode | Keluaran |
|---|---|---|
| tulis, buatkan, susun | Menulis | Teks baru, mengikuti protokol SKILL.md |
| perbaiki, rapikan, sunting, naturalkan, *humanize* | Menyunting | Teks hasil + catatan paling banyak tiga baris |
| periksa, cek, nilai, audit, "ini kayak AI nggak?" | Memeriksa | Daftar temuan, tanpa menulis ulang |

Kalau tidak jelas apakah pengguna ingin teksnya diubah, pilih memeriksa. Di akhir laporan boleh ada satu kalimat tawaran menyunting; ini satu-satunya tawaran lanjutan yang sah di paket ini.

Ada dua ragam yang perlu dibedakan: ragam teks yang digarap (menentukan aturan dan nilai `--ragam`) dan ragam jawabanmu kepada pengguna (mengikuti cara pengguna bicara).

## Aturan menyunting

1. **Isi tidak berubah.** Fakta, angka, tanggal, nama, kutipan langsung, tautan, kode, dan istilah teknis tetap persis sama. Aturan ini mengalahkan aturan gaya: jangan memadatkan frasa bila maknanya bisa bergeser ("mengumumkan peluncuran pada 3 November" belum tentu sama dengan "meluncurkan pada 3 November"); kalau ragu, pertahankan dan sebut di catatan.
2. **Jangan menambah.** Tidak ada contoh, data, atau pendapat baru. Kalimat kosong dihapus; jangan diganti klaim baru supaya terdengar spesifik. Kolom "Ganti dengan" di daftar frasa ditulis untuk mode menulis; di mode menyunting, arah gantinya adalah hapus, pakai fakta yang sudah ada di teks, atau minta datanya lewat catatan.
3. **Pertahankan suara dan ragam penulis.** Tentukan ragam dari teksnya, lalu ikuti. Campur kode yang disengaja, humor, dan logat penulis dibiarkan. Yang diseragamkan hanya ketidakkonsistenan (sapaan *Anda* bercampur *kamu*, istilah berganti-ganti).
4. **Potong dulu, baru ubah.** Sebagian besar slop hilang dengan dihapus, jadi hasil biasanya lebih pendek. Teks yang sudah baik dikembalikan nyaris utuh. Jangan menyunting supaya terlihat bekerja.
5. **Jangan sentuh** isi di dalam tanda petik kutipan langsung, blok kode, nama produk, judul karya, dan teks ragam beku (pasal, akad, doa). Atribusi di luar tanda petik boleh dirapikan.
6. **Hormati konvensi genre.** Salam surat resmi, tagar, struktur siaran pers, dan emoji penanda tetap ada; buang hanya yang berlebihan untuk genrenya. Bagian wajib genre yang belum ada (judul dan narahubung siaran pers, misalnya) disebut di catatan, jangan dikarang.
7. **Salah eja diperbaiki di semua ragam**, kecuali di dalam kutipan langsung.
8. **Skala mengikuti permintaan.** "Rapikan ejaannya" berarti ejaan saja; jangan menulis ulang gaya tanpa diminta.

## Langkah

1. Baca seluruh teks. Catat pembaca, ragam, sapaan, dan pesan utamanya.
2. Jalankan pemeriksa bila bisa (perintahnya ada di Pemeriksaan Wajib SKILL.md; skripnya `scripts/periksa.py` di folder bahasa-inti). Teks tempelan disimpan dulu ke berkas sementara.
3. Sunting dengan urutan ini: jejak asisten serta pembuka dan penutup ritual, lalu kalimat kosong, lalu pola kalimat ([frasa-terlarang.md](frasa-terlarang.md) bagian 5), lalu kosakata, kaidah, dan format.
4. Bandingkan fakta: setiap angka, nama, dan tautan pada teks asli harus ada di hasil, dan hasil tidak memuat yang baru.
5. Periksa pola pengganti (bagian 9 daftar yang sama), lalu jalankan pemeriksa sekali lagi pada hasilnya.

## Keluaran mode menyunting

Serahkan teks hasil lebih dulu, tanpa pengantar. Sesudahnya, paling banyak tiga baris catatan, hanya bila ada yang perlu diketahui pengguna: klaim tanpa sumber yang dibiarkan, bagian yang maknanya ambigu, atau informasi yang harus dilengkapi (harga, tanggal, alamat). Jangan mendaftar semua perubahan kecuali diminta.

## Keluaran mode memeriksa

1. Ringkasan satu atau dua kalimat: seberapa berat, dan pola apa yang dominan.
2. Temuan, diurutkan dari yang paling mengganggu pembaca. Tiap temuan: kutipan pendek, kode, dan arah perbaikan. Kode: L1 sampai L10 (Sepuluh Larangan Keras), EJ (ejaan dan kata baku), TB (tata bahasa), KS (konsistensi sapaan, istilah, ragam), PG (pola pengganti). Temuan dari skill kategori diberi label biasa, misalnya "SEO: janji judul tidak ditepati".
3. Satu baris tentang bagian yang sebaiknya tidak diubah, bila ada.

Arah perbaikan tidak boleh memuat data rekaan. Kalau perbaikannya butuh fakta, tulis "isi dengan angka dari timmu", jangan mencontohkan angka. Pemeriksaan kategori dipakai seperlunya: ambil yang terasa oleh pembaca (janji judul, CTA ganda), dan lewati butir teknis (panjang meta, jumlah H2) kecuali pengguna meminta audit. Pemeriksa otomatis dijalankan pada teks pengguna saja; laporanmu pasti memuat kutipan frasa bermasalah, jadi tidak perlu dipindai.

Contoh temuan:

> "Fitur ini bukan hanya cepat, tetapi juga hemat baterai" · L3 · tulis "Fitur ini cepat dan hemat baterai", atau sebut angkanya.

## Kalau ditanya "ini tulisan AI atau bukan?"

Jawab dengan pola yang ditemukan, lalu katakan terus terang bahwa pola tidak membuktikan asal-usul. Manusia menulis klise yang sama jauh sebelum ada model bahasa, dan tebakan pembaca maupun alat detektor sering keliru ke dua arah. Yang bisa dinilai dengan pasti adalah mutunya: kalimat mana yang kosong, dan bagaimana memperbaikinya.

## Kalau diminta "biar lolos detektor AI"

Paket ini menyunting untuk pembaca manusia. Jangan menjanjikan skor detektor mana pun, jangan menyelipkan salah ketik atau kalimat janggal supaya "terasa manusia", dan jangan memutar sinonim demi mengubah statistik teks. Untuk tugas kuliah dan naskah jurnal, arahkan pengguna ke aturan keterbukaan pemakaian AI di kampus atau jurnalnya; lihat `bahasa-peneliti`.
