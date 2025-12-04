# DATA BENSIN & KOTA
# Data bensin dan kota
bensin_data = {
    "Pertalite": {"harga": 10000, "jarak_tempuh": 12},
    "Pertamax": {"harga": 14000, "jarak_tempuh": 13},
    "Pertamax Turbo": {"harga": 17000, "jarak_tempuh": 13.5}
}

kota_data = {
    "jakarta": 20,
    "bekasi": 35.7,
    "depok": 5,
    "tangerang": 99,
    "bogor": 120.6
}

# Input dari pengguna
nama_kendaraan = input("Nama kendaraan? (mobil/motor): ").capitalize()
jenis_bensin = input("Jenis bensin? (Pertalite/Pertamax/Pertamax Turbo): ").title()
kota_tujuan = input("Kota yang dituju? (jakarta/bekasi/depok/tangerang/bogor): ").lower()

# # Ambil data
# jarak_kota = kota_data.get(kota_tujuan)
# data_bensin = bensin_data.get(jenis_bensin)

# if jarak_kota and data_bensin:
#     pemakaian_bensin = jarak_kota / data_bensin["jarak_tempuh"]
#     total_harga = pemakaian_bensin * data_bensin["harga"]

# Validasi input
if jenis_bensin in bensin_data and kota_tujuan in kota_data:
    jarak_kota = kota_data[kota_tujuan]
    harga_bensin = bensin_data[jenis_bensin]["harga"]
    jarak_tempuh = bensin_data[jenis_bensin]["jarak_tempuh"]

    pemakaian_bensin = jarak_kota / jarak_tempuh
    total_harga = pemakaian_bensin * harga_bensin

    # Output
    print("\n--- Rincian Perjalanan ---")
    print(f"Nama Kendaraan   : {nama_kendaraan}")
    print(f"Jenis Bensin     : {jenis_bensin}")
    print(f"Kota Tujuan      : {kota_tujuan.capitalize()}")
    print(f"Pemakaian Bensin : {pemakaian_bensin:.2f} liter")
    print(f"Total Harga      : Rp {total_harga:,.0f}")
else:
    print("Data tidak valid. Pastikan input sesuai pilihan yang tersedia.")