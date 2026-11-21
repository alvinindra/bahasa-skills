# Changelog

All notable changes to bahasa-skills are documented here. This project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format.

## [Unreleased]

## [1.4.0] - 2026-11-21

### Added

- Pemeriksa otomatis `skills/bahasa-inti/scripts/periksa.py` (Python 3, tanpa dependensi): memindai L1 sampai L10, kata nonbaku, kata depan dirangkai, tanda pisah, kata tugas berkapital di judul, batas hashtag, sapaan tercampur, jejak alat, dan pola pengganti; temuan dibagi KERAS dan TINJAU; opsi `--ragam`, `--seo`, `--ketat`, `--json`. Uji di `tests/` dan alur CI `test.yml`.
- `references/penyuntingan.md`: mode menyunting (isi dan suara penulis tidak berubah) dan mode memeriksa (laporan temuan), plus sikap terhadap permintaan "lolos detektor AI".
- Kategori baru di `frasa-terlarang.md`: jejak asisten ("Tentu! Berikut…", "Semoga membantu!"), kata pengisi (*tentunya, pastinya*), pertanyaan yang dijawab sendiri, pembuka bertahap, pengerucutan titik dua, kesimpulan kosong, sangkalan korektif, kiasan tekstil, rujukan kabur "hal ini/tersebut", pola pengganti, dan daftar "yang bukan slop".
- Bentuk terbalik paralelisme negatif ("Y, bukan X", "Y alih-alih X") masuk L3; kewajiban "ambil sikap".
- Instalasi lewat Skills CLI (`npx skills add alvinindra/bahasa-skills`) pada README.
- Petunjuk instalasi untuk Google Antigravity (global dan per proyek) pada `README.md`.
- Alur otomatisasi GitHub Actions (`.github/workflows/release.yml`) agar setiap commit yang dipush ke cabang `main` otomatis memperbarui tag rilis Git (`vX.Y.Z` dan `latest`) serta GitHub Release.
- Kerangka HSO (*Hook-Story-Offer*) dan FAB (*Feature-Advantage-Benefit*) pada referensi copywriting pemasaran.
- Panduan jembatan anti-bot (*anti-robot bridges*) dan tabel perbandingan hook AI vs manusia (masalah, angka, fitur, edukasi, B2B) pada referensi media sosial.

### Fixed

- **Kapital judul.** Versi sebelumnya menyebut gaya kalimat sebagai satu-satunya yang benar dan menghitung judul berkapital tiap kata sebagai slop. EYD V butir F.21 justru meminta kapital di tiap kata judul kecuali kata tugas. L10, `ejaan-eyd.md`, bahasa-seo, dan bahasa-website kini mengikuti EYD V; gaya kalimat tetap sah sebagai gaya selingkung yang seragam. `CONTOH.md` diberi catatan revisi.
- `memerhatikan` dicatat tidak baku (KBBI VI: *memperhatikan*); `tepercaya`, `produktivitas` ditambahkan ke `kata-baku.md`.
- Penulisan *maha-* dipastikan dari laman EYD V: terpisah dan berkapital (*Yang Maha Esa*).
- Rujukan domain `kemdikbud.go.id` (sudah tidak aktif) diganti `kemendikdasmen.go.id` untuk KBBI, EYD, dan PASTI.

### Changed

- Batas hashtag kini batas platform: Instagram (Desember 2025) dan TikTok membatasi 5 per unggahan.
- Aturan superlatif merujuk EPI Amandemen 2020 butir 1.2.2 beserta definisi buktinya; ditambah ketentuan *gratis*, *100%*, *halal*, *satu-satunya*.
- Syarat membaca `frasa-terlarang.md`, `kata-baku.md`, dan `ejaan-eyd.md` diseragamkan dan diringankan untuk teks pendek, setelah uji tulis dengan agen menunjukkan aturan antarskill tidak sejalan.
- Contoh teladan yang melanggar larangan paket sendiri (hook QRIS, pembuka artikel SEO) ditulis ulang.
- L6 tidak lagi menjatah transisi "satu kali per teks"; yang dilarang transisi di dua paragraf beruntun dan pengulangan dalam jarak dekat.
- Larangan tanda pisah dijelaskan sebagai keputusan gaya paket yang lebih ketat daripada EYD V; Wikipedia memindahkan tanda pisah ke indikator historis per September 2026.
- Klaim "hiruk pikuk tervalidasi penutur asli" diturunkan sesuai buktinya (satu unggahan Threads).
- Menghapus bagian versioning dan rilis dari `README.md` sehingga dokumentasi perubahan sepenuhnya berada di `CHANGELOG.md`.
- Memperluas daftar frasa pemasaran terlarang (L5 dan `frasa-terlarang.md`) untuk menangkal slop khas AI marketing seperti "kini hadir sebagai solusi", "tak perlu khawatir lagi", "siap menemani langkah Anda", "rasakan perbedaannya", dan pengandaian mengawang "bayangkan jika".
- Memperjelas bahwa angka, contoh, dan adegan faktual harus bersumber; contoh hook tidak lagi menyarankan angka rekaan.
- Memperbaiki aturan hook dan CTA media sosial agar pembuka terdengar alami dan ajakan menyimpan sesuai manfaat isi.
- Menambahkan rujukan riset tentang pola teks AI dengan batasan eksplisit bahwa temuan korpus bahasa Inggris tidak dapat dipakai sebagai detektor kalimat Indonesia.

## [1.3.0] - 2026-10-25

### Added

- Installation instructions for Codex and OpenCode, including global and project-level setup.

### Changed

- Simplified the router and core skill workflow to load only relevant references and avoid duplicate checks.
- Made the em dash prohibition explicit for formal and consultative writing.
