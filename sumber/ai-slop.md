# Sumber: Ciri Tulisan AI (AI Slop)

Dipakai untuk: Sepuluh Larangan Keras (bahasa-inti) dan seluruh isi frasa-terlarang.md.

Temuan metodologis penting: **tidak ada daftar frasa AI berbahasa Indonesia yang terkurasi di web** saat riset (Agustus 2026). Media Indonesia membahas ciri struktural umum, bukan daftar kata. Maka daftar frasa Indonesia di paket ini disusun dari tiga lapis: (1) butir yang terkonfirmasi sumber, (2) kalque dari daftar AI-slop Inggris yang terkonfirmasi, (3) pola keluaran LLM Indonesia yang dikenali. Lapisan 2 dan 3 bersifat kualitatif.

## Deteksi tulisan AI versi media Indonesia

- https://radvoice.id/blog/8-cara-mendeteksi-tulisan-yang-dibuat-ai/ [S]
- https://www.cnnindonesia.com/teknologi/20250711135904-185-1249601/cara-mendeteksi-tulisan-hasil-chatgpt-ini-ciri-cirinya [S]
- https://www.tempo.co/digital/4-ciri-tulisan-yang-dihasilkan-oleh-chatgpt-2025609 [S]
- https://www.detik.com/jateng/berita/d-7940641/5-cara-deteksi-tulisan-hasil-ai-dan-chatgpt-bisa-pakai-tools-ini [S]
- https://theconversation.com/mengapa-tulisan-asli-bisa-terdeteksi-buatan-ai-benarkah-deteksi-ai-tidak-akurat-pahami-cara-kerja-dan-tips-mengatasinya-248257 [P] · juga peringatan false positive (penulis manusia teliti ikut tertuduh)
- https://idntimes.com/life/education/annisa-nur-fitriani-1/tulisan-terindikasi-ai-padahal-ditulis-manual-c1c2 [S]
- https://www.threads.com/@jalanbarengintrovert/post/DX8_Fx1FHLY/ [S] · validasi penutur asli untuk "hiruk pikuk" sebagai penanda ChatGPT ("kalau ada 'hiruk pikuk', dijamin dari ChatGPT"); dasar larangan mutlak di L5

## Pola struktural (internasional, diadaptasi)

- https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing [P] · sumber utama: paralelisme negatif, rule of three, penghindaran kopula, klausa ekor, atribusi kabur, kesimpulan bergaya outline, Title Case, bold berlebihan, emoji bullet, em dash, jejak alat
- https://www.forbes.com/sites/jodiecook/2025/09/08/the-10-giveaway-signs-of-ai-writing-wikipedia-reveals/ [S]
- https://www.makeuseof.com/wikipedia-best-ai-writing-detection-guide/ [S]
- https://flowingdata.com/2025/10/20/signs-of-ai-writing-on-wikipedia/ [S]
- https://alstonantony.com/ai-seo/avoid-chatgpt-words-phrases-seo/ [S] · 300+ kata/frasa yang sering dipakai ChatGPT
- https://blog.atharvashah.com/p/the-ultimate-ai-slop-word-blacklist [S]
- https://www.oliviacal.com/post/ai-writing-tells [S]
- https://www.aicheckr.io/blog/ai-slop-examples [S]

## Kajian frekuensi kata (dasar kuantitatif)

- https://www.science.org/doi/10.1126/sciadv.adt3813 [A] · Kobak dkk., "Delving into LLM-assisted writing in biomedical publications through excess vocabulary", Science Advances (2025). 15,1 juta abstrak PubMed; kata dengan rasio kelebihan ekstrem: *delves* (28,0), *underscores* (13,8), *showcasing* (10,7); 379 "excess style words" (66% verba); estimasi minimal 13,5% abstrak 2024 diproses LLM
- https://arxiv.org/abs/2406.07016 [A] · pracetak studi yang sama
- https://pubmed.ncbi.nlm.nih.gov/40601754/ [A]
- https://pmejournal.org/articles/10.5334/pme.1929 [A] · studi pendamping tentang kosakata ber-AI di penulisan medis
- https://www.medrxiv.org/content/10.1101/2024.05.14.24307373.full.pdf [A]
- https://www.rollingstone.com/culture/culture-features/chatgpt-hypen-em-dash-ai-writing-1235314945/ [S] · em dash sebagai penanda; jadi meme "ChatGPT hyphen"
- https://news.fiu.edu/2026/why-does-ai-use-so-many-em-dashes-an-expert-explains [S]

## Catatan keandalan

1. **"Hiruk pikuk"** adalah satu-satunya penanda khas Indonesia yang tervalidasi penutur asli secara organik; karena itu dijadikan larangan prioritas tertinggi.
2. **Em dash**: model tertentu kini bisa disuruh berhenti memakainya, jadi ketiadaan em dash bukan bukti tulisan manusia. Paket ini tetap melarangnya sebagai tanda baca gaya karena kehadirannya tetap penanda kuat, dan bahasa Indonesia memang jarang memakainya di luar rentang.
3. **Belum ada studi korpus excess-vocabulary untuk bahasa Indonesia** (Garuda, SINTA, korpus berita). Daftar frasa Indonesia bersifat kualitatif; revisi saat studi semacam itu terbit.
4. Jangan menjadikan "tulisan terlalu rapi/tanpa typo" sebagai penanda AI: menghukum penulis manusia yang teliti (false positive yang dikeluhkan sumber The Conversation dan IDN Times).
