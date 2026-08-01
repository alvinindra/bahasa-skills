---
name: bahasa-skills
description: "Pemandu paket bahasa-skills. WAJIB dipakai pada SETIAP tugas menulis, menyunting, menerjemahkan, atau menilai teks berbahasa Indonesia, apa pun bentuknya: caption, iklan, email, copy situs, microcopy, artikel SEO, laporan, skripsi, jurnal, dokumentasi, pesan. Skill ini membaca kebutuhan dari prompt lalu mengarahkan ke aturan inti anti AI-slop dan skill kategori yang cocok (marketing/media sosial, website/UX writing, SEO, karya ilmiah). Gunakan meski pengguna tidak menyebut nama skill; cukup terdeteksi bahwa keluarannya teks bahasa Indonesia. (Router for ALL Indonesian-language writing tasks.)"
---

# bahasa-skills: Pemandu Arah

Paket ini terdiri dari satu fondasi dan empat spesialisasi. Tugasmu di sini ada tiga: kenali jenis permintaan, muat aturan yang tepat, lalu jalankan protokolnya sampai pemeriksaan akhir. Jangan menulis sebelum aturan termuat.

## Langkah pemakaian

1. **Selalu baca [skills/bahasa-inti/SKILL.md](skills/bahasa-inti/SKILL.md) lebih dulu.** Larangan anti-slop, pemilihan ragam, dan Pemeriksaan Wajib di sana berlaku untuk semua jenis teks, tanpa kecuali.
2. **Cocokkan permintaan dengan tabel arah di bawah**, lalu baca SKILL.md kategori yang cocok. Baca berkas `references/` yang disebut skill kategori itu sesuai kebutuhan tugas.
3. **Ikuti protokol**: empat keputusan awal (pembaca, ragam, medium, satu pesan), tulis, lalu jalankan Pemeriksaan Wajib bahasa-inti plus pemeriksaan tambahan kategori. Teks yang belum lolos belum boleh diserahkan.

## Tabel arah

Tentukan kategori dari **bentuk keluaran** yang diminta, bukan dari topiknya. Artikel tentang produk tetap artikel (SEO); caption tentang riset tetap caption (marketing).

| Sinyal pada prompt | Kategori | Baca |
|---|---|---|
| caption, konten sosmed, IG/TikTok/X/LinkedIn/Facebook, iklan, promo, tagline, email marketing/blast, brand voice, kalender konten, jualan, soft selling | Marketing | [skills/bahasa-marketing/SKILL.md](skills/bahasa-marketing/SKILL.md) |
| copy website, landing page, microcopy, UX writing, tombol, pesan error/galat, empty state, form, onboarding, notifikasi, halaman produk/tentang kami/FAQ/404, company profile | Website | [skills/bahasa-website/SKILL.md](skills/bahasa-website/SKILL.md) |
| artikel SEO, konten blog, riset keyword/kata kunci, search intent, title tag, meta description, heading, featured snippet, optimasi konten, content plan | SEO | [skills/bahasa-seo/SKILL.md](skills/bahasa-seo/SKILL.md) |
| skripsi, tesis, jurnal, karya ilmiah, laporan penelitian, proposal riset, abstrak, tinjauan pustaka, metodologi, parafrase akademik, sitasi, daftar pustaka | Peneliti | [skills/bahasa-peneliti/SKILL.md](skills/bahasa-peneliti/SKILL.md) |
| email biasa, surat, dokumentasi, pesan, pengumuman, terjemahan umum, penyuntingan umum, "perbaiki tulisan ini", "bikin lebih natural" | Inti saja | cukup bahasa-inti + references-nya |

## Kasus campuran

Pilih satu kategori utama dari medium tempat teks akan tayang, lalu pinjam referensi kategori lain seperlunya:

- **Landing page yang menjual**: Website sebagai utama (struktur halaman, microcopy), tambah [skills/bahasa-marketing/references/copywriting.md](skills/bahasa-marketing/references/copywriting.md) untuk nada penawaran, CTA, dan aturan klaim.
- **Artikel blog yang mempromosikan produk**: SEO sebagai utama, tambah copywriting.md untuk bagian penawarannya. Aturan superlatif marketing tetap berlaku.
- **Laporan riset untuk klien (bukan jurnal)**: Peneliti untuk kejujuran data dan sitasi; ragam boleh turun ke konsultatif mengikuti empat keputusan awal bahasa-inti.
- **Email**: penawaran memakai Marketing; transaksional/onboarding produk memakai Website; email kerja biasa cukup Inti.
- **Naskah video/skrip konten**: Marketing (rujuk bagian TikTok di media-sosial.md).

## Kalau ragu

- Ragu antara dua kategori: putuskan dari medium tayang. Masih seri, pilih yang pemeriksaan tambahannya lebih ketat, lalu sebutkan asumsimu ke pengguna.
- Informasi yang menentukan arah tulisan tidak ada (sapaan merek, ragam, platform, audiens): ajukan satu pertanyaan singkat. Salah ragam lebih mahal daripada satu pertanyaan.
- Tidak ada kategori yang cocok: jalankan bahasa-inti saja secara penuh.

## Peta berkas

```
skills/
├── bahasa-inti/            # WAJIB untuk semua tugas
│   └── references/         # frasa-terlarang, kata-baku, padanan-istilah, ejaan-eyd
├── bahasa-marketing/
│   └── references/         # media-sosial, copywriting
├── bahasa-website/
│   └── references/         # ux-writing, halaman-situs
├── bahasa-seo/
│   └── references/         # riset-kata-kunci, on-page
└── bahasa-peneliti/
    └── references/         # kalimat-akademik, struktur-sitasi
```

Satu pengingat terakhir: paket ini menilai mutu dari spesifisitas. Kalimat yang bisa dipakai untuk topik apa pun adalah kalimat yang harus ditulis ulang, di kategori mana pun.
