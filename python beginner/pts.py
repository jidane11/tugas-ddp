# Input dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operator = input("Pilih operator (+, -, /, *, **): ")

# Proses perhitungan
if operator == "+":
    hasil = angka1 + angka2
    simbol = "+"
    nama_operator = "tambah"
elif operator == "-":
    hasil = angka1 - angka2
    simbol = "-"
    nama_operator = "kurang"
elif operator == "/":
    hasil = angka1 / angka2
    simbol = "/"
    nama_operator = "bagi"
elif operator == "*":
    hasil = angka1 * angka2
    simbol = "x"
    nama_operator = "kali"
elif operator == "**":
    hasil = angka1 ** angka2
    simbol = "**"
    nama_operator = "pangkat"
else:
    hasil = "Operator tidak valid"
    nama_operator = "tidak dikenali"
    simbol = "?"

# Output hasil
print("\nAngka pertama :", angka1)
print("Angka kedua   :", angka2)
print("Pilihan Operator :", nama_operator)

if isinstance(hasil, (int, float)):
    print(f"Hasil operator {angka1} {simbol} {angka2} = {hasil}")
else:
    print(hasil)