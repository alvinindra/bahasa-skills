#!/usr/bin/env python3
"""Analisis eksperimen bahasa-skills (lihat protokol.md).

  python3 penelitian/analisis.py ukur      # jalankan pemeriksa atas 24 naskah
  python3 penelitian/analisis.py paket     # susun paket juri buta + kunci acak
  python3 penelitian/analisis.py analisis  # statistik dan tabel

Hanya pustaka standar. Pemeriksa yang dipakai adalah salinan beku versi tag
v1.4.0 (data/periksa_v1_4_0.py), supaya hasil bisa diulang walau skrip di
skills/ berubah.
"""

import importlib.util
import itertools
import json
import math
import pathlib
import random
import statistics
import sys

SINI = pathlib.Path(__file__).resolve().parent
DATA = SINI / "data"
KONDISI = ["K", "G", "S"]
NAMA = {"K": "kontrol", "G": "generik", "S": "skill"}
BENIH = 20261121


def muat_pemeriksa():
    spec = importlib.util.spec_from_file_location("periksa", DATA / "periksa_v1_4_0.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def muat_prompt():
    return json.loads((DATA / "prompt.json").read_text(encoding="utf-8"))


def naskah(kondisi, pid):
    return (DATA / "keluaran" / kondisi / f"{pid}.txt").read_text(encoding="utf-8")


def ukur():
    periksa = muat_pemeriksa()
    hasil = {}
    for p in muat_prompt():
        for k in KONDISI:
            temuan, st = periksa.periksa(naskah(k, p["id"]), p["ragam"], p["seo"])
            kata = st["kata"]
            hasil[f"{k}-{p['id']}"] = {
                "kondisi": k, "prompt": p["id"], "kata": kata,
                "keras": st["keras"], "tinjau": st["tinjau"],
                "keras_per_100": round(100 * st["keras"] / kata, 3) if kata else None,
                "tinjau_per_100": round(100 * st["tinjau"] / kata, 3) if kata else None,
                "temuan": [{"kode": t["kode"], "tingkat": t["tingkat"], "nama": t["nama"],
                            "kutipan": t["kutipan"]} for t in temuan],
            }
    (DATA / "hasil_pemeriksa.json").write_text(
        json.dumps(hasil, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("tersimpan: data/hasil_pemeriksa.json")


def paket():
    acak = random.Random(BENIH)
    kunci, bagian = {}, []
    for p in muat_prompt():
        urutan = KONDISI[:]
        acak.shuffle(urutan)
        kunci[p["id"]] = dict(zip("ABC", urutan))
        bagian.append(f"## Tugas {p['id']}\n\n### Brief dari pemberi tugas\n\n{p['prompt']}\n")
        for label, k in zip("ABC", urutan):
            bagian.append(f"### Naskah {p['id']}-{label}\n\n<<<AWAL NASKAH>>>\n{naskah(k, p['id']).strip()}\n<<<AKHIR NASKAH>>>\n")
    (DATA / "kunci_acak.json").write_text(json.dumps(kunci, indent=2) + "\n", encoding="utf-8")
    (DATA / "paket_juri.md").write_text("# Paket penilaian\n\n" + "\n".join(bagian), encoding="utf-8")
    print("tersimpan: data/paket_juri.md, data/kunci_acak.json")


def uji_tanda(selisih):
    """Uji permutasi tanda berpasangan yang eksak, dua sisi."""
    amati = abs(sum(selisih))
    n = len(selisih)
    ekstrem = sum(1 for tanda in itertools.product((1, -1), repeat=n)
                  if abs(sum(t * d for t, d in zip(tanda, selisih))) >= amati - 1e-12)
    return ekstrem / 2 ** n


def binomial_atas(k, n, p):
    """P(X >= k) untuk X ~ Binomial(n, p)."""
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))


def analisis():
    hasil = json.loads((DATA / "hasil_pemeriksa.json").read_text(encoding="utf-8"))
    kunci = json.loads((DATA / "kunci_acak.json").read_text(encoding="utf-8"))
    prompt = [p["id"] for p in muat_prompt()]
    ringkas = {"per_kondisi": {}, "uji": {}, "juri": {}}

    print("### Temuan pemeriksa per naskah (KERAS / TINJAU / kata)\n")
    print("| Prompt | " + " | ".join(NAMA[k] for k in KONDISI) + " |")
    print("|---|---|---|---|")
    for pid in prompt:
        sel = [hasil[f"{k}-{pid}"] for k in KONDISI]
        print(f"| {pid} | " + " | ".join(f"{h['keras']} / {h['tinjau']} / {h['kata']}" for h in sel) + " |")

    print("\n### Ringkasan per kondisi\n")
    print("| Kondisi | Rerata KERAS/100 kata | Median | Rerata TINJAU/100 kata | Total KERAS | Total kata | Naskah tanpa KERAS |")
    print("|---|---|---|---|---|---|---|")
    for k in KONDISI:
        h = [hasil[f"{k}-{pid}"] for pid in prompt]
        kp = [x["keras_per_100"] for x in h]
        tp = [x["tinjau_per_100"] for x in h]
        r = {"rerata_keras_per_100": round(statistics.mean(kp), 2), "median_keras_per_100": round(statistics.median(kp), 2),
             "rerata_tinjau_per_100": round(statistics.mean(tp), 2), "total_keras": sum(x["keras"] for x in h),
             "total_tinjau": sum(x["tinjau"] for x in h), "total_kata": sum(x["kata"] for x in h),
             "naskah_tanpa_keras": sum(x["keras"] == 0 for x in h)}
        ringkas["per_kondisi"][k] = r
        print(f"| {NAMA[k]} | {r['rerata_keras_per_100']:.2f} | {r['median_keras_per_100']:.2f} | "
              f"{r['rerata_tinjau_per_100']:.2f} | {r['total_keras']} | {r['total_kata']} | {r['naskah_tanpa_keras']}/8 |")

    print("\n### Uji permutasi tanda berpasangan (KERAS per 100 kata)\n")
    for a, b in (("S", "K"), ("S", "G"), ("G", "K")):
        d = [hasil[f"{a}-{pid}"]["keras_per_100"] - hasil[f"{b}-{pid}"]["keras_per_100"] for pid in prompt]
        p = uji_tanda(d)
        r = {"rerata_selisih": round(statistics.mean(d), 2), "p_dua_sisi": round(p, 4),
             "lebih_rendah": sum(x < 0 for x in d), "sama": sum(x == 0 for x in d), "lebih_tinggi": sum(x > 0 for x in d)}
        ringkas["uji"][f"{a}-{b}"] = r
        print(f"- {NAMA[a]} dikurangi {NAMA[b]}: rerata selisih {r['rerata_selisih']:.2f}; {r['lebih_rendah']} prompt lebih rendah, "
              f"{r['sama']} sama, {r['lebih_tinggi']} lebih tinggi; p = {p:.4f}")

    berkas_juri = sorted(DATA.glob("juri_*.json"))
    if berkas_juri:
        print("\n### Juri buta\n")
        pertama_semua, pilihan = {k: 0 for k in KONDISI}, []
        klaim = {k: 0 for k in KONDISI}
        jumlah_peringkat = {k: 0 for k in KONDISI}
        for bj in berkas_juri:
            j = json.loads(bj.read_text(encoding="utf-8"))
            pertama = {k: 0 for k in KONDISI}
            pilih = {}
            for pid in prompt:
                for label, peringkat in j[pid]["peringkat"].items():
                    k = kunci[pid][label]
                    jumlah_peringkat[k] += peringkat
                    if peringkat == 1:
                        pertama[k] += 1
                        pilih[pid] = k
                for label, daftar in j[pid].get("klaim_luar_brief", {}).items():
                    klaim[kunci[pid][label]] += len(daftar)
            pilihan.append(pilih)
            for k in KONDISI:
                pertama_semua[k] += pertama[k]
            p = binomial_atas(pertama["S"], len(prompt), 1 / 3)
            ringkas["juri"][bj.stem] = {"peringkat_pertama": pertama, "p_binomial_S": round(p, 4)}
            print(f"- {bj.stem}: peringkat pertama " + ", ".join(f"{NAMA[k]} {pertama[k]}" for k in KONDISI)
                  + f"; P(X >= {pertama['S']} | n = 8, p = 1/3) = {p:.4f}")
        n = len(prompt) * len(berkas_juri)
        p = binomial_atas(pertama_semua["S"], n, 1 / 3)
        sepakat = sum(pilihan[0].get(pid) == pilihan[1].get(pid) for pid in prompt) if len(pilihan) == 2 else None
        ringkas["juri"]["gabungan"] = {
            "peringkat_pertama": pertama_semua, "n": n, "p_binomial_S": round(p, 6),
            "rerata_peringkat": {k: round(jumlah_peringkat[k] / n, 2) for k in KONDISI},
            "klaim_luar_brief_menurut_juri": klaim, "sepakat_peringkat_pertama": sepakat}
        print(f"- gabungan ({n} penilaian): " + ", ".join(f"{NAMA[k]} {pertama_semua[k]}" for k in KONDISI)
              + f"; P(X >= {pertama_semua['S']} | n = {n}, p = 1/3) = {p:.6f}")
        print("- rerata peringkat (1 terbaik): " + ", ".join(f"{NAMA[k]} {jumlah_peringkat[k] / n:.2f}" for k in KONDISI))
        print("- klaim di luar brief menurut juri (jumlah butir, dua juri): " + ", ".join(f"{NAMA[k]} {klaim[k]}" for k in KONDISI))
        if sepakat is not None:
            print(f"- kedua juri memilih naskah peringkat pertama yang sama pada {sepakat} dari {len(prompt)} prompt")

    (DATA / "ringkasan.json").write_text(json.dumps(ringkas, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    perintah = {"ukur": ukur, "paket": paket, "analisis": analisis}
    if len(sys.argv) != 2 or sys.argv[1] not in perintah:
        sys.exit(__doc__)
    perintah[sys.argv[1]]()
