# Laporan: Efektivitas bahasa-skills v1.4.0

Eksperimen terdaftar (protokol di-commit sebelum pengambilan data). Desain dan pertanyaan penelitian ada di [protokol.md](protokol.md); berkas ini hanya berisi hasil dan pembahasannya. Semua naskah mentah, keluaran pemeriksa, kunci acak, dan jawaban juri tersimpan di [data/](data/).

## Cara menjalankan ulang

```bash
python3 penelitian/analisis.py ukur      # hitung temuan pemeriksa per naskah
python3 penelitian/analisis.py paket     # susun ulang paket juri (benih 20261121)
python3 penelitian/analisis.py analisis  # semua angka di laporan ini
```

## Hasil pemeriksa otomatis

KERAS/TINJAU/jumlah kata per naskah:

| Prompt | Kontrol | Generik | Skill |
|---|---|---|---|
| M1 | 3 / 1 / 106 | 0 / 0 / 94 | 0 / 0 / 121 |
| M2 | 0 / 1 / 105 | 2 / 1 / 150 | 0 / 1 / 179 |
| W1 | 0 / 0 / 34 | 0 / 0 / 33 | 0 / 1 / 79 |
| W2 | 0 / 1 / 148 | 0 / 1 / 176 | 0 / 1 / 141 |
| S1 | 0 / 0 / 62 | 0 / 0 / 67 | 0 / 0 / 97 |
| S2 | 0 / 1 / 256 | 0 / 1 / 265 | 0 / 0 / 336 |
| P1 | 0 / 0 / 101 | 0 / 1 / 111 | 0 / 0 / 161 |
| I1 | 0 / 2 / 92 | 0 / 1 / 92 | 0 / 1 / 158 |

| Kondisi | Rerata KERAS/100 kata | Total KERAS | Total kata | Naskah tanpa KERAS |
|---|---|---|---|---|
| Kontrol | 0,35 | 3 | 904 | 7/8 |
| Generik | 0,17 | 2 | 988 | 7/8 |
| Skill | 0,00 | 0 | 1.272 | 8/8 |

Uji permutasi tanda berpasangan atas KERAS per 100 kata (dua sisi):

| Perbandingan | Rerata selisih | p |
|---|---|---|
| Skill − kontrol | −0,35 | 1,0000 |
| Skill − generik | −0,17 | 1,0000 |
| Generik − kontrol | −0,19 | 1,0000 |

H1 dan H2 **tidak terkonfirmasi**: temuan KERAS terlalu sedikit di semua kondisi (3, 2, dan 0 dari total 24 naskah) untuk dibedakan secara statistik; semua selisih bergantung pada satu prompt. Arahnya konsisten (skill paling rendah) tetapi tidak bermakna.

## Hasil juri buta

Dua sesi juri (subagen terpisah, hanya melihat brief dan naskah A/B/C beracak; kunci di `data/kunci_acak.json`) memberi peringkat 1–3 per trio.

Peringkat pertama per juri:

| Juri | Kontrol | Generik | Skill | P(X ≥ yang teramati \| n = 8, p = 1/3) |
|---|---|---|---|---|
| Juri 1 | 3 | 2 | 3 | 0,5318 |
| Juri 2 | 0 | 3 | 5 | 0,0879 |
| Gabungan (n = 16) | 3 | 5 | 8 | 0,1265 |

Rerata peringkat gabungan (1 terbaik): kontrol 2,19; generik 2,00; skill 1,81.

H3 **tidak terkonfirmasi** pada α = 0,05 (p gabungan 0,127), walau arahnya mendukung skill. Kedua juri memilih naskah peringkat pertama yang sama hanya pada 3 dari 8 prompt — persetujuan antarjuri rendah, jadi penilaian "siap pakai" di sini sebagian besar selera.

## Klaim di luar brief

Juri mencatat butir klaim yang melewati isi brief (daftar lengkap di `juri_1.json` dan `juri_2.json`): kontrol 19 butir, generik 30, skill 30 — tidak ada keunggulan skill. Dua catatan penting:

- Naskah skill untuk S2 menulis rujukan hukum yang tidak ada di brief ("UU Nomor 1 Tahun 2022", "PP Nomor 76 Tahun 2020") sebagai ganti angka tarif. Skill melarang mengarang rujukan; pelanggaran ini terjadi justru di kondisi skill. Keduanya adalah dasar hukum yang nyata dan relevan, tetapi tetap klaim di luar brief yang tidak diminta.
- Banyak butir "klaim luar brief" adalah inferensi wajar dari brief (misalnya menghitung Rp700.000 dari Rp350 × 2.000 lembar, atau menjelaskan konsekuensi penghapusan data). Hitungan mentahnya melebih-lebihkan masalah; tetapi tanpa panduan penilaian ketat, angka ini sendiri bukti keterbatasan ukuran.

## Hal yang teramati di luar hipotesis

- Naskah kondisi skill konsisten **lebih panjang** (1.272 kata vs 904 dan 988). Sebagian karena agen menambahkan catatan kepatutan (misalnya "nomor WhatsApp ada di bio") yang memang dianjurkan skill — itu perilaku yang diinginkan, tetapi membuat kondisi ini bisa dikenali pembaca teliti dan memperlemah pembutaan.
- Enam dari delapan naskah skill memuat catatan batasan atau asumsi untuk pengguna; satu naskah kontrol dan satu generik melakukannya.
- Temuan TINJAU per 100 kata: kontrol 0,64; generik 0,45; skill 0,40 — arahnya sama dengan KERAS, sama-sama tidak konklusif.

## Penyimpangan dari protokol

- Paket juri sempat tertulis ke dalam repo lalu dipindah ke `/tmp/bs-studi/paket_juri.md` sebelum juri dijalankan; juri tidak membaca repo. Kunci acak tetap di repo (`data/kunci_acak.json`).
- Tidak ada penyimpangan lain; prompt, kondisi, dan ukuran sesuai protokol.

## Keterbatasan

- Satu percobaan per sel; satu kelompok model penulis (subagen, model tidak diumumkan) dan dua juri dari kelompok yang sama. Hasil tidak bisa digeneralisasi ke model lain atau juri manusia.
- Pemeriksa otomatis mengukur katalog pola yang ia kenal — bukan "kualitas" — dan katalog itu bagian dari skill sendiri, sehingga ukuran ini agak bias memihak skill. Meski begitu selisihnya tidak signifikan.
- Persetujuan antarjuri rendah (3/8); peringkat "siap pakai" perlu diraih dengan panduan penilaian yang lebih ketat atau juri manusia.
- Delapan prompt mencakup lima bentuk tulisan; bentuk lain (siaran pers, terjemahan, dokumen teknis) tidak diuji.

## Kesimpulan

Pada 24 naskah dari 24 agen: kondisi skill menghasilkan nol temuan KERAS (vs 2–3 pada pembanding) dan cenderung lebih disukai juri buta (8/16 peringkat pertama vs harapan 5,3), tetapi tidak ada satu pun selisih yang signifikan pada ukuran ini. Temuan ini **petunjuk arah, bukan bukti**; kejutan negatifnya — naskah skill menambahkan rujukan hukum di luar brief — menunjukkan aturan "jangan menambah fakta" belum cukup kuat dan layak dipertajam.
