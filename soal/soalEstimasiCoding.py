# Program Estimasi Waktu Praktikum Coding

# Input data
nama = input("Nama mahasiswa: ")
jumlah_latihan = int(input("Jumlah latihan: "))
menit_per_latihan = int(input("Menit per latihan: "))
waktu_tersedia = int(input("Waktu tersedia (menit): "))

# Proses perhitungan
total_waktu = jumlah_latihan * menit_per_latihan
sisa_waktu = waktu_tersedia - total_waktu
cukup_waktu = total_waktu <= waktu_tersedia

# Operator ternary
status = "Cukup" if cukup_waktu else "Tidak cukup"

# Output hasil
print()
print("===== ESTIMASI PRAKTIKUM =====")
print("Nama:", nama)
print("Total waktu latihan:", total_waktu, "menit")
print("Sisa waktu:", sisa_waktu, "menit")
print("Waktu cukup:", cukup_waktu)
print("Status:", status)