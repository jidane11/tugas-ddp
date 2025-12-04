

# # # Menu makanan
# makanan = {
#     "nasi goreng": 15000,
#     "mie goreng": 12000,
#     "ayam geprek": 18000
# }

# # Menu minuman
# minuman = {
#     "aneka jus": 15000,
#     "soft drink": 10000,
#     "sweet ice tea": 5000
# }

# nama = input("Masukkan Nama Pembeli: ")
# no_hp = input("Masukkan No HP Pembeli: ")

# kategori = input("Pesan menu apa? (makanan/minuman): ").lower()

# # Tampilkan menu sesuai pilihan
# if kategori == "makanan":
#     print("\n--- MENU MAKANAN ---")
#     for m, h in makanan.items():
#         print(m.title(), "Rp", h)
#     pesanan = input("Masukkan pesanan: ").lower()
#     harga = makanan[pesanan]

# elif kategori == "minuman":
#     print("\n--- MENU MINUMAN ---")
#     for m, h in minuman.items():
#         print(m.title(), "Rp", h)
#     pesanan = input("Masukkan pesanan: ").lower()
#     harga = minuman[pesanan]

# jumlah = int(input("Masukkan jumlah pesanan: "))

# total = harga * jumlah

# print("\n=== STRUK PEMBAYARAN ===")
# print("Nama Pembeli :", nama)
# print("No HP        :", no_hp)
# print("Menu Pesanan :", pesanan.title())
# print("Jumlah       :", jumlah)
# print("Total Bayar  : Rp", total)


# Menu makanan
makanan = {
    "nasi goreng": 15000,
    "mie goreng": 12000,
    "ayam geprek": 18000
}

# Menu minuman
minuman = {
    "aneka jus": 15000,
    "soft drink": 10000,
    "sweet ice tea": 5000
}

# Input data pembeli
nama = input("Masukkan Nama Pembeli: ")
no_hp = input("Masukkan No HP Pembeli: ")

kategori = input("Pesan menu apa? (makanan/minuman): ").lower()

# Inisialisasi variabel
pesanan = ""
harga = 0

# Tampilkan menu sesuai pilihan
if kategori == "makanan":
    print("\n--- MENU MAKANAN ---")
    for m, h in makanan.items():
        print(m.title(), "Rp", h)
    pesanan = input("Masukkan pesanan: ").lower()
    if pesanan in makanan:
        harga = makanan[pesanan]
    else:
        print("Pesanan tidak tersedia di menu makanan.")
        exit()

elif kategori == "minuman":
    print("\n--- MENU MINUMAN ---")
    for m, h in minuman.items():
        print(m.title(), "Rp", h)
    pesanan = input("Masukkan pesanan: ").lower()
    if pesanan in minuman:
        harga = minuman[pesanan]
    else:
        print("Pesanan tidak tersedia di menu minuman.")
        exit()
else:
    print("Kategori tidak valid. Silakan pilih 'makanan' atau 'minuman'.")
    exit()

# Input jumlah pesanan
jumlah = int(input("Masukkan jumlah pesanan: "))

# Hitung total
total = harga * jumlah

# Cetak struk
print("\n=== STRUK PEMBAYARAN ===")
print("Nama Pembeli :", nama)
print("No HP        :", no_hp)
print("Menu Pesanan :", pesanan.title())
print("Jumlah       :", jumlah)
print("Total Bayar  : Rp", total)