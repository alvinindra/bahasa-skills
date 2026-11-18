# Changelog

All notable changes to bahasa-skills are documented here. This project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format.

## [Unreleased]

### Added

- Petunjuk instalasi untuk Google Antigravity (global dan per proyek) pada `README.md`.
- Alur otomatisasi GitHub Actions (`.github/workflows/release.yml`) agar setiap commit yang dipush ke cabang `main` otomatis memperbarui tag rilis Git (`vX.Y.Z` dan `latest`) serta GitHub Release.
- Kerangka HSO (*Hook-Story-Offer*) dan FAB (*Feature-Advantage-Benefit*) pada referensi copywriting pemasaran.
- Panduan jembatan anti-bot (*anti-robot bridges*) dan tabel perbandingan hook AI vs manusia (masalah, angka, fitur, edukasi, B2B) pada referensi media sosial.

### Changed

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
