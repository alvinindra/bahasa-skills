"""Uji pemeriksa slop. Jalankan: python3 -m unittest discover -s tests"""

import importlib.util
import pathlib
import re
import unittest

AKAR = pathlib.Path(__file__).resolve().parent.parent
INTI = AKAR / "skills" / "bahasa-inti"
spec = importlib.util.spec_from_file_location("periksa", INTI / "scripts" / "periksa.py")
periksa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(periksa)


def kode(teks, ragam=None, tingkat=None):
    temuan, _ = periksa.periksa(teks, ragam)
    return [t["kode"] for t in temuan if tingkat is None or t["tingkat"] == tingkat]


def nama(teks, ragam=None):
    return [t["nama"] for t in periksa.periksa(teks, ragam)[0]]


class LaranganKeras(unittest.TestCase):
    def test_pembuka_klise(self):
        self.assertIn("L1", kode("Di era digital yang serba cepat ini, bisnis berubah."))
        self.assertIn("L1", kode("Seiring perkembangan teknologi, cara belanja ikut berubah."))
        self.assertIn("L1", kode("Tak bisa dimungkiri, harga naik."))

    def test_penutup_ritual(self):
        self.assertIn("L2", kode("Semoga bermanfaat!"))
        self.assertIn("L2", kode("Jadi, tunggu apa lagi?"))

    def test_paralelisme_negatif(self):
        self.assertIn("L3", kode("Aplikasi ini bukan hanya cepat, tetapi juga hemat baterai."))
        self.assertIn("L3", kode("Caption bukan sekadar teks, ia sarana membangkitkan emosi."))
        self.assertIn("L3", kode("Digitalisasi bukan lagi pilihan, melainkan keharusan."))

    def test_tripel_kata_sifat(self):
        self.assertIn("L4", kode("Layanan kami cepat, mudah, dan terjangkau."))
        self.assertNotIn("L4", kode("Kamu butuh domain, hosting, dan CMS."))

    def test_kosakata_slop(self):
        for teks in ("Di tengah hiruk pikuk kota.", "Ini sangat krusial.", "Mari menyelami topiknya.",
                     "Kini hadir Kasirin untuk UMKM.", "Bawa bisnismu ke level berikutnya."):
            self.assertIn("L5", kode(teks), teks)
        self.assertNotIn("L5", kode("Lanskap Bromo berubah setelah erupsi."))

    def test_transisi_beruntun(self):
        teks = "Selain itu, biayanya turun.\n\nOleh karena itu, kami pindah.\n"
        self.assertIn("L6", kode(teks))
        self.assertNotIn("L6", kode("Biayanya turun.\n\nOleh karena itu, kami pindah.\n"))

    def test_meta_dan_pengisi(self):
        self.assertIn("L7", kode("Artikel ini akan membahas cara menabung."))
        self.assertIn("L7", kode("Penting untuk dicatat bahwa harga berubah."))

    def test_atribusi_kabur(self):
        self.assertIn("L8", kode("Para ahli menilai tren ini berlanjut."))
        self.assertNotIn("L8", kode("Kobak dkk. (2025) menemukan 379 kata berlebih."))

    def test_jejak_asisten(self):
        self.assertIn("L9", kode("Tentu! Berikut caption untuk produk Anda."))
        self.assertIn("L9", kode("Semoga membantu."))
        self.assertIn("L9", kode("Pertanyaan yang sangat bagus."))

    def test_superlatif_hanya_tinjau(self):
        self.assertIn("L9", kode("Sabun terlaris di kategori ini.", tingkat="TINJAU"))
        self.assertNotIn("L9", kode("Sabun terlaris di kategori ini.", tingkat="KERAS"))


class Format(unittest.TestCase):
    def test_tanda_pisah(self):
        self.assertIn("L10", kode("Toko ini—yang baru buka—ramai.", tingkat="KERAS"))
        self.assertIn("L10", kode("Periode 2019—2022 dicatat.", tingkat="TINJAU"))
        self.assertNotIn("L10", kode("Periode 2019—2022 dicatat.", tingkat="KERAS"))
        self.assertIn("L10", kode("Periode 2019—2022 dicatat.", ragam="resmi", tingkat="KERAS"))

    def test_judul_eyd(self):
        self.assertIn("kata tugas berhuruf kapital di judul", nama("# Dampak Teknologi Dan Digitalisasi"))
        self.assertEqual([], kode("# Cara Mengatur Keuangan Rumah Tangga dengan Gaji UMR"))
        self.assertEqual([], kode("# Cara mengatur keuangan rumah tangga"))
        self.assertEqual([], kode("Judul: Dari Ave Maria ke Jalan Lain ke Roma"))
        teks = "Cara Mengatur Keuangan Rumah Tangga: 50/30/20 Untuk Gaji UMR\n\nRumus ini membagi gaji jadi tiga pos.\n"
        self.assertIn("kata tugas berhuruf kapital di judul", nama(teks))
        self.assertEqual(2, nama("# 5 Tips Memilih Laptop Untuk Mahasiswa Yang Tepat").count(
            "kata tugas berhuruf kapital di judul"))
        self.assertEqual([], kode("Kasirin sekarang bisa terima QRIS\n\nBiayanya gratis sampai Oktober.\n"))
        self.assertEqual([], kode("Ia Pergi Ke Pasar.\n"))

    def test_panjang_judul_seo(self):
        panjang = "# Cara Mengatur Keuangan Rumah Tangga dengan Gaji UMR Pakai Rumus 50/30/20\n"
        self.assertIn("judul lebih dari 60 karakter", [t["nama"] for t in periksa.periksa(panjang, seo=True)[0]])
        self.assertNotIn("judul lebih dari 60 karakter", nama(panjang))

    def test_hashtag(self):
        self.assertIn("hashtag berlebih", nama("Promo. #a1 #b2 #c3 #d4 #e5 #f6"))
        self.assertNotIn("hashtag berlebih", nama("Promo. #a1 #b2 #c3 #d4 #e5"))
        self.assertIn("hashtag generik", nama("Promo. #fyp"))

    def test_jejak_alat_dan_templat(self):
        self.assertIn("jejak alat", nama("Harga naik. :contentReference[oaicite:1]{index=1}"))
        self.assertIn("templat belum diisi", nama("Halo [Nama Pelanggan], pesananmu dikirim."))
        self.assertEqual([], kode("Angka ini belum dicek. [RUJUKAN DIPERLUKAN: data BI 2025]"))

    def test_frontmatter_dan_kode_dilewati(self):
        teks = "---\nname: x\ndescription: Di era digital ini\n---\n\n```\nsemoga bermanfaat\n```\nIsi `resiko` bersih.\n"
        self.assertEqual([], kode(teks))


class EjaanDanTataBahasa(unittest.TestCase):
    def test_kata_baku(self):
        for salah in ("silahkan", "resiko", "mempraktekkan", "menganalisa", "beresiko", "merubah",
                      "mempengaruhi", "memerhatikan", "terpercaya", "dimana", "kerjasama", "ketrampilan",
                      "dipersilahkan", "merespon", "berhutang", "elit"):
            self.assertIn("EJ", kode(f"Kata {salah} muncul."), salah)

    def test_bukan_salah_eja(self):
        for benar in ("Seekor rubah lewat.", "Silakan masuk.", "Ia memperhatikan detail.",
                      "Risiko kecil.", "Kami bekerja sama.", "Layanan tepercaya.",
                      "Penelitian ini melibatkan 40 responden.", "Sistemnya responsif dan kompleks.",
                      "Ia bernapas lega.", "Pemahaman peserta naik."):
            self.assertNotIn("EJ", kode(benar), benar)

    def test_anda_kapital(self):
        self.assertIn("Anda tanpa kapital", nama("Silakan cek email anda."))
        self.assertNotIn("Anda tanpa kapital", nama("Silakan cek email Anda."))

    def test_penghubung_dan_pleonasme(self):
        self.assertIn("TB", kode("Sistem yang mana harus diganti."))
        self.assertIn("TB", kode("Ini adalah merupakan masalah."))
        self.assertIn("TB", kode("Meskipun hujan, tetapi ia datang."))

    def test_sapaan_tercampur(self):
        self.assertIn("sapaan tercampur", nama("Tingkatkan bisnis Anda. Kamu bisa mulai gratis."))
        self.assertNotIn("sapaan tercampur", nama('Pembeli bertanya, "Anda buka?" Kamu jawab: buka.'))

    def test_ragam_formal(self):
        self.assertIn("KS", kode("Hasilnya nggak signifikan.", ragam="resmi"))
        self.assertNotIn("KS", kode("Hasilnya nggak signifikan.", ragam="santai"))


class Sinkron(unittest.TestCase):
    def test_teks_bersih(self):
        teks = ("Ada pembeli di warungmu pegang HP. \"Bisa bayar QRIS?\" Kamu jawab apa?\n\n"
                "Kasirin sekarang terima pembayaran QRIS dari aplikasi yang biasa kamu pakai.\n\n"
                "Buka aplikasi Kasirin, lalu aktifkan QRIS di menu pembayaran.\n\n#kasirin #qriswarung\n")
        self.assertEqual([], kode(teks, tingkat="KERAS"))

    def test_daftar_nonbaku_ada_di_referensi(self):
        rujukan = (INTI / "references" / "kata-baku.md").read_text(encoding="utf-8").lower()
        hilang = [k for k in list(periksa.NONBAKU) + list(periksa.NONBAKU_UTUH)
                  if not re.search(r"(?<![a-z])" + re.escape(k) + r"(?![a-z])", rujukan)]
        self.assertEqual([], hilang, "kata di periksa.py belum tercantum di kata-baku.md")

    def test_kode_keluar(self):
        import contextlib, io, tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".txt", encoding="utf-8", delete=False) as f:
            f.write("Semoga bermanfaat!\n")
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(0, periksa.main([f.name]))
            self.assertEqual(1, periksa.main(["--ketat", f.name]))
        pathlib.Path(f.name).unlink()

if __name__ == "__main__":
    unittest.main()
