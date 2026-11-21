---
name: bahasa-skills
description: "Pemandu paket bahasa-skills. WAJIB dipakai pada SETIAP tugas menulis, menyunting, menerjemahkan, atau menilai teks berbahasa Indonesia, apa pun bentuknya: caption, iklan, email, copy situs, microcopy, artikel SEO, laporan, skripsi, jurnal, dokumentasi, pesan; juga untuk permintaan 'biar nggak kayak AI', 'humanize', atau 'cek tulisan ini'. Skill ini membaca kebutuhan dari prompt lalu mengarahkan ke aturan inti anti AI-slop dan skill kategori yang cocok (marketing/media sosial, website/UX writing, SEO, karya ilmiah). Gunakan meski pengguna tidak menyebut nama skill; cukup terdeteksi bahwa keluarannya teks bahasa Indonesia. (Router for ALL Indonesian-language writing tasks.)"
---

# bahasa-skills: Pemandu Arah

Paket ini terdiri dari satu fondasi dan empat spesialisasi. Tugasmu di sini ada tiga: kenali jenis permintaan, muat aturan yang tepat, lalu jalankan protokolnya sampai pemeriksaan akhir. Jangan menulis sebelum aturan termuat.

## Alur singkat

1. Tentukan mode (menulis, menyunting, atau memeriksa saja) dan kategori dari bentuk keluaran yang diminta.
2. Baca [skills/bahasa-inti/SKILL.md](skills/bahasa-inti/SKILL.md) dan SKILL.md kategori utama. Untuk tugas campuran, pilih satu kategori utama lalu gunakan aturan tambahan yang memang diperlukan.
3. Baca hanya `references/` yang relevan menurut tabel di tiap skill.
4. Tulis, lalu periksa draf dengan pemeriksaan inti dan pemeriksaan kategori yang sesuai. Kalau perintah bisa dijalankan, pakai pemeriksa otomatis `skills/bahasa-inti/scripts/periksa.py` (path relatif terhadap folder berkas ini; jalankan dengan path absolut) untuk pindaian kata dan tanda baca. Lewati butir yang tidak relevan dengan tugas; jangan mengulang pemeriksaan yang sama.
5. Serahkan naskahnya saja, tanpa pengantar dan tanpa tawaran lanjutan. Asumsi dicatat singkat sesudah naskah. Di mode memeriksa, keluarannya laporan temuan.

## Tabel arah

Tentukan kategori dari **bentuk keluaran** yang diminta, bukan dari topiknya. Artikel tentang produk tetap artikel (SEO); caption tentang riset tetap caption (marketing).

| Sinyal pada prompt | Kategori | Baca |
|---|---|---|
| caption, konten sosmed, IG/TikTok/X/LinkedIn/Facebook, iklan, promo, tagline, email marketing/blast, brand voice, kalender konten, jualan, soft selling | Marketing | [skills/bahasa-marketing/SKILL.md](skills/bahasa-marketing/SKILL.md) |
| copy website, landing page, microcopy, UX writing, tombol, pesan error/galat, empty state, form, onboarding, notifikasi, halaman produk/tentang kami/FAQ/404, company profile | Website | [skills/bahasa-website/SKILL.md](skills/bahasa-website/SKILL.md) |
| artikel SEO, konten blog, riset keyword/kata kunci, search intent, title tag, meta description, heading, featured snippet, optimasi konten, content plan | SEO | [skills/bahasa-seo/SKILL.md](skills/bahasa-seo/SKILL.md) |
| skripsi, tesis, jurnal, karya ilmiah, laporan penelitian, proposal riset, abstrak, tinjauan pustaka, metodologi, parafrase akademik, sitasi, daftar pustaka | Peneliti | [skills/bahasa-peneliti/SKILL.md](skills/bahasa-peneliti/SKILL.md) |
| email biasa, surat, siaran pers, dokumentasi, pesan, pengumuman, terjemahan umum | Inti saja | cukup bahasa-inti + references-nya |
| teks jadi yang diserahkan untuk diperbaiki atau dinilai: "perbaiki tulisan ini", "bikin lebih natural", "biar nggak kayak AI", "cek tulisan ini" | Inti (mode menyunting/memeriksa) + kategori sesuai bentuk teksnya | [skills/bahasa-inti/references/penyuntingan.md](skills/bahasa-inti/references/penyuntingan.md) |

## Kasus campuran

Pilih satu kategori utama dari medium tempat teks akan tayang, lalu pinjam referensi kategori lain seperlunya:

- **Landing page yang menjual**: Website sebagai utama (struktur halaman, microcopy), tambah [skills/bahasa-marketing/references/copywriting.md](skills/bahasa-marketing/references/copywriting.md) untuk nada penawaran, CTA, dan aturan klaim.
- **Artikel blog yang mempromosikan produk**: SEO sebagai utama, tambah copywriting.md untuk bagian penawarannya. Aturan superlatif marketing tetap berlaku.
- **Laporan riset untuk klien (bukan jurnal)**: Peneliti untuk kejujuran data dan sitasi; ragam boleh turun ke konsultatif mengikuti empat keputusan awal bahasa-inti.
- **Siaran pers peluncuran produk**: Inti dengan ragam resmi; aturan klaim dan superlatif Marketing tetap berlaku.
- **Email**: penawaran memakai Marketing; transaksional/onboarding produk memakai Website; email kerja biasa cukup Inti.
- **Naskah video/skrip konten**: Marketing (rujuk bagian TikTok di media-sosial.md).

## Kalau ragu

- Ragu antara dua kategori: putuskan dari medium tayang. Masih seri, pilih yang pemeriksaan tambahannya lebih ketat, lalu sebutkan asumsimu ke pengguna.
- Informasi yang menentukan arah tulisan tidak ada (sapaan merek, ragam, platform, audiens): ajukan satu pertanyaan singkat. Salah ragam lebih mahal daripada satu pertanyaan.
- Detail pelengkap tidak ada (cara aktivasi, syarat promo, kanal CTA): jangan dikarang. Tulis versi yang paling wajar, lalu catat sebagai asumsi sesudah naskah.
- Tidak ada kategori yang cocok: jalankan bahasa-inti saja secara penuh.

## Hemat konteks

Dalam satu sesi, jangan baca ulang berkas yang sudah tersedia di konteks. Tabel referensi tiap skill menjelaskan kapan sebuah berkas diperlukan.

Satu pengingat terakhir: paket ini menilai mutu dari spesifisitas. Kalimat yang bisa dipakai untuk topik apa pun adalah kalimat yang harus ditulis ulang, di kategori mana pun.
