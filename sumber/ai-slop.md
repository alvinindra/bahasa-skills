# Sumber: Ciri Tulisan AI (AI Slop)

Dipakai untuk: Sepuluh Larangan Keras (bahasa-inti), seluruh isi frasa-terlarang.md, penyuntingan.md, dan daftar pola di `scripts/periksa.py`.

Riset pertama: Agustus 2026. Riset kedua: 21 November 2026 (ditandai **[Nov 2026]**).

Temuan metodologis: sampai November 2026 **belum ada studi korpus kosakata berlebih untuk bahasa Indonesia**. Daftar frasa Indonesia di paket ini disusun dari tiga lapis: (1) butir yang disebut sumber berbahasa Indonesia, (2) kalque dari daftar berbahasa Inggris yang terdokumentasi, (3) pola keluaran LLM berbahasa Indonesia yang dikenali penyusun. Lapis 2 dan 3 bersifat kualitatif.

## Deteksi tulisan AI versi media dan penyunting Indonesia

- https://warungfiksi.net/misi-menangkap-basah-tulisan-hasil-ai/ [P] **[Nov 2026]** · Brahmanto Anindito (penulis dan penyunting), April 2026. Sepuluh ciri dari meja sunting: "bukan hanya… tapi juga", tanda pisah untuk sisipan, transisi klise, metafora tekstil ("permadani kehidupan", "merajut masa depan"), "mengungkap misteri", tiga serangkai, "menyelami", kata sifat dramatis ("sangat krusial"), simile berlebihan, penutup ajakan mengawang. Dasar butir kiasan tekstil, simile, dan "mengungkap" di frasa-terlarang.md.
- https://aidetectors.cc/id/blog/gemini-vs-chatgpt-style [S] **[Nov 2026]** · beda kebiasaan antarmodel dalam teks Indonesia: Gemini mengulang "dapat …" dan "perlu diperhatikan bahwa …", ChatGPT "merupakan hal yang penting" dan "dapat dikatakan bahwa …"; penutup penyeimbang vs penutup ringkasan; sikap kabur. Situs penjual alat deteksi, jadi dipakai hanya untuk pengamatan polanya.
- https://rum.web.id/2026/02/ciri-tulisan-yang-dihasilkan-ai-jujur-ini-bikin-agak-jengkel [S] **[Nov 2026]** · anak kalimat mendahului induk kalimat sebagai pembuka, "bukan sekadar … ia menjelma …", pengerucutan dengan titik dua. Hanya cuplikan hasil pencarian yang terbaca; halamannya gagal dibuka saat riset.
- https://kiosmaya.com/ciri-ciri-artikel-yang-terlihat-dibuat-dengan-chatgpt/ [S] **[Nov 2026]** · pembuka "Banyak orang yang belum menyadari bahwa…", penutup "Pada akhirnya, semua tergantung pada preferensi masing-masing".
- https://www.jawapos.com/teknologi/2509060265/5-cara-mudah-bedakan-tulisan-chatgpt-dengan-manusia-betulan-dari-bahasa-yang-terlalu-rapi-hingga-gaya-tanda-baca-yang-janggal [S] **[Nov 2026]**
- https://radvoice.id/blog/8-cara-mendeteksi-tulisan-yang-dibuat-ai/ [S]
- https://www.cnnindonesia.com/teknologi/20250711135904-185-1249601/cara-mendeteksi-tulisan-hasil-chatgpt-ini-ciri-cirinya [S]
- https://www.tempo.co/digital/4-ciri-tulisan-yang-dihasilkan-oleh-chatgpt-2025609 [S]
- https://www.detik.com/jateng/berita/d-7940641/5-cara-deteksi-tulisan-hasil-ai-dan-chatgpt-bisa-pakai-tools-ini [S]
- https://theconversation.com/mengapa-tulisan-asli-bisa-terdeteksi-buatan-ai-benarkah-deteksi-ai-tidak-akurat-pahami-cara-kerja-dan-tips-mengatasinya-248257 [P] · juga peringatan false positive (penulis manusia teliti ikut tertuduh)
- https://idntimes.com/life/education/annisa-nur-fitriani-1/tulisan-terindikasi-ai-padahal-ditulis-manual-c1c2 [S]
- https://www.threads.com/@jalanbarengintrovert/post/DX8_Fx1FHLY/ [S] · seorang penutur menyebut "hiruk pikuk" sebagai penanda ChatGPT ("kalau ada 'hiruk pikuk', dijamin dari ChatGPT")
- https://www.linkedin.com/posts/ivanlanin_detektor-tulisan-ai-bahasa-indonesia-activity-7271297429105197056---0p [P] **[Nov 2026]** · Ivan Lanin menguji 17 detektor tulisan AI untuk bahasa Indonesia (Desember 2024). Hanya judul dan tautannya yang terbaca; isi artikel Medium-nya belum diperiksa, jadi tidak dikutip sebagai dasar aturan.

## Skill sejenis

- https://github.com/Adamfatur/lugas [P] **[Nov 2026]** · skill penyunting teks Indonesia (lisensi MIT) dengan katalog 31 pola, pemeriksa regex, dan uji buta. Yang dipelajari dari sana: perlunya mode sunting yang menjaga isi, kategori "sapaan chatbot", "kata pengisi" (*tentunya, pastinya*), "pertanyaan yang dijawab sendiri", "hal ini/tersebut" berulang, dan pemeriksa otomatis. Kode pemeriksa paket ini ditulis sendiri dan cakupannya berbeda (kode L1 sampai L10, kata baku, kapital judul, batas hashtag, pola pengganti).
- https://github.com/syahiidkamil/Software-Engineer-AI-Agent-Atlas/blob/main/.claude/skills/human-writing/languages/id.md [S] **[Nov 2026]** · modul bahasa Indonesia sebuah skill umum; tujuannya "tidak terdeteksi sebagai AI", yang tidak diikuti paket ini.

## Pola struktural (internasional, diadaptasi)

- https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing [P] · sumber utama. Dibaca ulang **[Nov 2026]**; perubahan penting sejak riset pertama:
  - "Overuse of em dashes (2022–September 2026)" kini masuk **indikator historis**. Model baru menekan tanda pisah, dan halaman itu mencatat akibatnya: variasi tanda baca turun, tinggal koma dan titik. Dasar bagian "Pola pengganti".
  - Paralelisme negatif kini punya subbentuk "Y rather than X", disebut makin lazim pada keluaran terbaru. Dasar larangan bentuk terbalik di L3.
  - "Hedging disclaimers … Mid-2026–present": sangkalan korektif ("should be treated as … rather than …", "does not establish …"). Dasar butir "sangkalan korektif".
  - "Signs of human writing": frasa *is/has* sederhana, kata biasa alih-alih sinonim kaku, superlatif, kata penguat, dan konstruksi agak boros lebih sering muncul di tulisan manusia. "Ineffective indicators": tata bahasa sempurna, prosa formal, dan kata transisi lepas bukan penanda yang sah. Dasar bagian "Yang bukan slop".
  - "Promotional language (2023–2025)", "Section summaries", dan "Elegant variation" juga pindah ke indikator historis; kosakata khas bergeser per generasi model.
  - Peringatan: kemampuan manusia membedakan teks LLM mendekati tebakan acak pada beberapa studi; alat detektor punya galat yang tidak kecil.
- https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/ [A] · analisis sekitar 490 ribu halaman web berbahasa Inggris; pola tingkat korpus (tanda baca, frasa, paralelisme negatif). Bukan alat untuk menilai satu kalimat, tidak menguji bahasa Indonesia.
- https://www.forbes.com/sites/jodiecook/2025/09/08/the-10-giveaway-signs-of-ai-writing-wikipedia-reveals/ [S]
- https://www.makeuseof.com/wikipedia-best-ai-writing-detection-guide/ [S]
- https://flowingdata.com/2025/10/20/signs-of-ai-writing-on-wikipedia/ [S]
- https://alstonantony.com/ai-seo/avoid-chatgpt-words-phrases-seo/ [S] · 300+ kata/frasa yang sering dipakai ChatGPT
- https://blog.atharvashah.com/p/the-ultimate-ai-slop-word-blacklist [S]
- https://www.oliviacal.com/post/ai-writing-tells [S]
- https://www.aicheckr.io/blog/ai-slop-examples [S]

## Kajian kuantitatif

- https://www.science.org/doi/10.1126/sciadv.adt3813 [A] · Kobak dkk., "Delving into LLM-assisted writing in biomedical publications through excess vocabulary", Science Advances (2025). 15,1 juta abstrak PubMed; kata dengan rasio kelebihan ekstrem: *delves* (28,0), *underscores* (13,8), *showcasing* (10,7); 379 "excess style words" (66% verba); estimasi minimal 13,5% abstrak 2024 diproses LLM
- https://arxiv.org/abs/2406.07016 [A] · pracetak studi yang sama
- https://arxiv.org/abs/2510.15061 [A] **[Nov 2026]** · Paech dkk., "Antislop: A Comprehensive Framework for Identifying and Eliminating Repetitive Patterns in Language Models" (2025). Slop diukur sebagai rasio frekuensi pola pada keluaran LLM terhadap teks manusia; sebagian pola muncul lebih dari 1.000 kali lebih sering. Mendukung pendekatan daftar pola per model, dan menunjukkan bahwa pelarangan token secara kasar merusak mutu.
- https://pubmed.ncbi.nlm.nih.gov/40601754/ [A]
- https://pmejournal.org/articles/10.5334/pme.1929 [A]
- https://www.medrxiv.org/content/10.1101/2024.05.14.24307373.full.pdf [A]
- https://journal.unnes.ac.id/journals/sji/article/download/27732/6304/112087 [A] **[Nov 2026]** · perbandingan esai siswa SMA dan esai ChatGPT berbahasa Indonesia (IndoBERT + fitur linguistik): esai siswa lebih beragam secara linguistik, esai ChatGPT lebih seragam dalam koherensi dan formalitas.
- https://journal.unpas.ac.id/index.php/pendas/article/view/65123 [A] **[Nov 2026]** · analisis kualitatif teks akademik mahasiswa vs teks AI berbahasa Indonesia: pola kalimat kaku, struktur logika berulang, tanpa konteks pengalaman.
- https://itiis.org/digital-library/manuscript/file/108184/TIIS%20Vol%2020,%20No%209-8.pdf [A] **[Nov 2026]** · bias detektor teks AI bahasa Indonesia terhadap penulis nonpenutur asli; dasar sikap "skor detektor bukan ukuran mutu".
- https://www.rollingstone.com/culture/culture-features/chatgpt-hypen-em-dash-ai-writing-1235314945/ [S] · em dash sebagai penanda; jadi meme "ChatGPT hyphen"
- https://news.fiu.edu/2026/why-does-ai-use-so-many-em-dashes-an-expert-explains [S]

## Penulisan skill

- https://agentskills.io/specification [P] **[Nov 2026]** · batas `name` dan `description` (1.024 karakter), SKILL.md di bawah 500 baris, folder `scripts/` dan `references/`, pemuatan bertahap.
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices [P] **[Nov 2026]** · ringkas, uji di semua model yang dipakai.
- https://github.com/vercel-labs/skills [P] **[Nov 2026]** · Skills CLI (`npx skills add`) dan aturan penemuan skill dalam repo.

## Catatan keandalan

1. **"Hiruk pikuk"**: dasar tertulisnya satu unggahan Threads. Larangannya dipertahankan karena murah dipatuhi, tetapi jangan diklaim sebagai temuan riset.
2. **Tanda pisah**: Wikipedia memindahkannya ke indikator historis per September 2026. Paket ini tetap melarangnya sebagai tanda baca gaya karena penulis Indonesia jarang memakainya, padahal EYD V mengizinkannya untuk mengapit keterangan. Ini keputusan gaya paket, lebih ketat daripada kaidah.
3. **Kapital judul**: versi sebelum November 2026 menyebut gaya kalimat sebagai satu-satunya yang benar dan menghitung Title Case sebagai pelanggaran. Itu meniru Manual of Style Wikipedia bahasa Inggris dan bertentangan dengan EYD V butir F.21. Sudah dikoreksi: yang salah adalah kata tugas berkapital dan gaya yang bercampur.
4. **Belum ada studi korpus kosakata berlebih untuk bahasa Indonesia** (Garuda, SINTA, korpus berita). Daftar frasa Indonesia bersifat kualitatif; revisi saat studi semacam itu terbit.
5. Kosakata khas bergeser tiap generasi model. Daftar kata diperlakukan sebagai potret, dan pola struktur (bagian 5 dan 9 frasa-terlarang.md) lebih awet daripada daftar kata.
6. Jangan menjadikan "tulisan terlalu rapi/tanpa typo" sebagai penanda AI: menghukum penulis manusia yang teliti.
7. Pola per model dari aidetectors.cc berasal dari satu sumber komersial tanpa data terbuka; dipakai sebagai contoh frasa, tidak sebagai klaim tentang model tertentu.
