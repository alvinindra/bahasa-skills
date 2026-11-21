# Protokol Penelitian

Ditulis dan di-commit pada 21 November 2026 **sebelum** satu pun naskah uji dibuat. Perubahan sesudah pengambilan data dicatat di bagian "Penyimpangan dari protokol" pada naskah, tidak dengan menyunting berkas ini.

## Pertanyaan penelitian

Apakah paket bahasa-skills v1.4.0 menurunkan jumlah pola slop dan salah tulis pada teks bahasa Indonesia yang ditulis agen berbasis model bahasa, dibandingkan dengan tanpa instruksi dan dengan satu kalimat instruksi generik?

## Hipotesis

- H1: temuan KERAS per 100 kata pada kondisi skill lebih rendah daripada kondisi kontrol.
- H2: temuan KERAS per 100 kata pada kondisi skill lebih rendah daripada kondisi instruksi generik.
- H3: juri buta menempatkan naskah kondisi skill di peringkat pertama "siap pakai" lebih sering daripada peluang acak (1/3).

## Rancangan

Eksperimen dalam-subjek dengan prompt sebagai unit: 8 prompt, masing-masing dikerjakan pada 3 kondisi, sehingga ada 24 naskah. Prompt tersimpan di `data/prompt.json` (2 pemasaran, 2 situs, 2 SEO, 1 akademik, 1 email kerja). Semua merek dan lembaga di dalamnya fiktif, dan fakta yang boleh dipakai dibatasi di dalam prompt supaya klaim di luar brief bisa dihitung.

| Kondisi | Instruksi untuk agen penulis |
|---|---|
| K (kontrol) | Prompt pengguna apa adanya; dilarang membaca berkas dan mencari di web. |
| G (generik) | Prompt pengguna + "Tulis senatural mungkin, hindari klise dan pola kalimat yang terasa seperti tulisan AI."; larangan yang sama. |
| S (skill) | Agen membaca pemandu `SKILL.md`, bahasa-inti, skill kategori, dan referensi yang relevan dari salinan bersih tag `v1.4.0`, lalu mengikuti protokolnya, termasuk menjalankan `periksa.py` bila bisa. |

Tiap naskah ditulis oleh satu subagen terpisah tanpa konteks bersama. Agen menyimpan jawaban lengkapnya (termasuk pengantar atau catatan bila ada) ke satu berkas. Satu percobaan per sel; tidak ada pengulangan dan tidak ada pemilihan hasil terbaik.

## Ukuran

1. **Utama: temuan KERAS per 100 kata**, dihitung `skills/bahasa-inti/scripts/periksa.py` versi tag `v1.4.0` atas jawaban lengkap, dengan `--ragam` (dan `--seo` untuk prompt SEO) yang sudah ditetapkan per prompt di `data/prompt.json`.
2. Temuan TINJAU per 100 kata, dari pemeriksa yang sama.
3. **Peringkat juri buta.** Dua subagen juri yang tidak membaca skill menerima brief dan tiga naskah per prompt dengan label A, B, C yang diacak (benih acak 20261121). Juri memeringkat naskah dari yang paling layak langsung dipakai pemberi tugas tanpa disunting (1) sampai yang paling tidak layak (3).
4. **Klaim di luar brief.** Juri yang sama mendaftar klaim faktual pada tiap naskah yang tidak ada di brief (angka, nama, waktu, fitur, syarat). Daftar itu diperiksa ulang oleh penyusun.

## Keterbatasan yang sudah diketahui sebelum data diambil

- **Sirkularitas ukuran utama.** Pemeriksa yang menjadi alat ukur adalah bagian dari perlakuan: agen kondisi S menjalankannya dan memperbaiki temuannya. Ukuran utama karena itu menjawab "apakah agen yang diberi skill menghasilkan naskah yang lolos pemeriksa", dan tidak membuktikan mutu secara mandiri. Ukuran 3 dan 4 ditambahkan sebagai pembanding yang tidak dihitung pemeriksa.
- Penulis, juri, dan penyusun adalah model bahasa dari keluarga yang sama. Tidak ada penilai manusia.
- Delapan prompt terlalu sedikit untuk kesimpulan statistik yang kuat; uji statistik dilaporkan sebagai eksploratif.
- Model di balik subagen tidak bisa dipastikan dari dalam sesi dan tidak bisa divariasikan.
- Agen pada semua kondisi diminta menyimpan jawabannya ke berkas, yang mungkin mengubah gaya jawaban dibanding percakapan biasa.

## Analisis

- Statistik deskriptif per kondisi (rerata, median) dan tabel per prompt.
- H1 dan H2: uji permutasi tanda berpasangan yang eksak (dua sisi) atas selisih temuan KERAS per 100 kata, n = 8 pasang (256 kemungkinan tanda).
- H3: jumlah peringkat pertama untuk kondisi S dari 16 penilaian (8 prompt × 2 juri), dibandingkan dengan peluang 1/3 memakai uji binomial eksak satu sisi. Karena dua juri menilai prompt yang sama, uji ini dilaporkan juga per juri (n = 8).
- Kesepakatan antarjuri: proporsi prompt dengan pilihan peringkat pertama yang sama.
- Taraf 0,05 tanpa koreksi uji ganda; seluruh hasil dibaca sebagai eksploratif.

## Aturan pengecualian

Jawaban yang tidak berisi naskah (menolak, atau hanya bertanya balik) dicatat apa adanya, tidak diganti dengan percobaan baru, dan prompt itu dikeluarkan dari uji berpasangan yang melibatkan kondisinya.

Semua naskah mentah, kunci acak, jawaban juri, dan skrip analisis disimpan di `penelitian/data/` dan `penelitian/analisis.py`.
