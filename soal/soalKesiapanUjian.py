# Program Evaluasi Kesiapan Mengikuti Ujian Praktikum

# Konstanta
MIN_NILAI = 75
MIN_KEHADIRAN = 80
PERANGKAT_WAJIB = "laptop"

# Input data
nama = input("Nama mahasiswa: ")
nilai_latihan = int(input("Nilai latihan: "))
jumlah_kehadiran = int(input("Jumlah kehadiran: "))
total_pertemuan = int(input("Total pertemuan: "))
perangkat = input("Perangkat yang dibawa: ")

# Proses perhitungan
persentase_kehadiran = jumlah_kehadiran / total_pertemuan * 100

# Proses pengecekan
nilai_memenuhi = nilai_latihan >= MIN_NILAI
kehadiran_memenuhi = persentase_kehadiran >= MIN_KEHADIRAN
perangkat_memenuhi = PERANGKAT_WAJIB in perangkat.lower()

# Operator logika
siap_ujian = nilai_memenuhi and kehadiran_memenuhi and perangkat_memenuhi

# Operator unary
belum_siap = not siap_ujian

# Operator ternary
status = "Siap ujian praktikum" if siap_ujian else "Belum siap ujian praktikum"

# Output hasil
print()
print("===== EVALUASI UJIAN PRAKTIKUM =====")
print("Nama:", nama)
print("Nilai latihan:", nilai_latihan)
print("Persentase kehadiran:", persentase_kehadiran, "%")
print("Perangkat wajib terpenuhi:", perangkat_memenuhi)
print("Siap ujian:", siap_ujian)
print("Belum siap:", belum_siap)
print("Status:", status)