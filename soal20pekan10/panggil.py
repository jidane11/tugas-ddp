import bangun_datar, bangun_ruang

print("====Luas Bangun Datar====")
print(f"Luas Persegi: {bangun_datar.luas_persegi(5)}")
print(f"Luas Segitiga: {bangun_datar.luas_segitiga(4, 6)}")
print(f"Luas Lingkaran: {bangun_datar.luas_lingkaran(7)}")
print(f"Luas Ketupat: {bangun_datar.luas_ketupat(6, 8)}")
print(f"Luas Jajar Genjang: {bangun_datar.luas_jajar_genjang(5, 10)}")

print("\n====Luas Bangun Ruang====")
print(f"Luas Kubus: {bangun_ruang.luas_kubus(4)}")
print(f"Luas Balok: {bangun_ruang.luas_balok(4, 5, 6)}")
print(f"Luas Bola: {bangun_ruang.luas_bola(7)}")
print(f"Luas Tabung: {bangun_ruang.luas_tabung(7, 10)}")
print(f"Luas Kerucut: {bangun_ruang.luas_kerucut(7, 10)}")