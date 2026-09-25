# Program Biodata Mahasiswa

# Konstanta
PROGRAM_STUDI = "Teknik Informatika"

# Input data dari pengguna
nama = input("Masukkan nama mahasiswa: ")
nim = input("Masukkan NIM: ")
umur = int(input("Masukkan umur: "))
ipk = float(input("Masukkan IPK: "))

# Output data
print("*** BIODATA MAHASISWA UVERS***")
print("Nama          :", nama)
print("NIM           :", nim)
print("Program Studi :", PROGRAM_STUDI)
print("Umur          :", umur, "tahun")
print("IPK           :", ipk)
print(f"nama saya {nama} umur saya {umur}")