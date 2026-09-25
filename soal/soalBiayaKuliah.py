# Program Perhitungan Biaya Kuliah Semester

# Konstanta biaya
BIAYA_PER_SKS = 150000
MAKSIMAL_SKS = 24
BIAYA_ADMINISTRASI = 50000
BIAYA_PRAKTIKUM = 200000

# Input data mahasiswa
nama = input("Masukkan nama mahasiswa: ")
nim = input("Masukkan NIM: ")
jumlah_sks = int(input("Masukkan jumlah SKS yang diambil: "))

# Proses perhitungan biaya
biaya_sks = jumlah_sks * BIAYA_PER_SKS
total_biaya = biaya_sks + BIAYA_ADMINISTRASI + BIAYA_PRAKTIKUM

# Operator ternary untuk menentukan status SKS
status_sks = "Valid" if jumlah_sks <= MAKSIMAL_SKS else "Melebihi batas maksimal"

# Output informasi biaya
print()
print("=== INFORMASI BIAYA KULIAH ===")
print("Biaya per SKS                 : Rp", BIAYA_PER_SKS)
print("Maksimal SKS per semester     :", MAKSIMAL_SKS, "SKS")
print("Biaya administrasi semester   : Rp", BIAYA_ADMINISTRASI)
print("Biaya praktikum semester      : Rp", BIAYA_PRAKTIKUM)

# Output rincian biaya mahasiswa
print()
print("=== RINCIAN BIAYA MAHASISWA ===")
print("Nama Mahasiswa                :", nama)
print("NIM                           :", nim)
print("Jumlah SKS yang Diambil       :", jumlah_sks, "SKS")
print("Status Pengambilan SKS        :", status_sks)
print("Biaya SKS                     : Rp", biaya_sks)
print("Total Biaya Semester          : Rp", total_biaya)