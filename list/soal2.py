
# SOAL 2 - PEMINJAMAN SEPEDA KAMPUS

# Membuat list kosong
durasi_peminjaman = []

print("===== PENCATATAN PEMINJAMAN SEPEDA =====")
print()

# Input durasi secara berulang
while True:
    durasi = int(input("Masukkan durasi peminjaman (menit): "))

    # Berhenti jika input 0
    if durasi == 0:
        break

    # Menolak durasi negatif
    if durasi < 0:
        print("Durasi tidak valid")
        continue

    # Menambahkan durasi ke dalam list
    durasi_peminjaman.append(durasi)

# Menampilkan hasil
print()
print("===== REKAP PEMINJAMAN =====")

# Memeriksa apakah list memiliki data
if len(durasi_peminjaman) > 0:

    # Menghitung statistik
    jumlah = len(durasi_peminjaman)
    total = sum(durasi_peminjaman)
    rata_rata = total / jumlah
    terlama = max(durasi_peminjaman)

    print("Daftar durasi:", durasi_peminjaman)
    print()
    print("Jumlah peminjaman:", jumlah)
    print("Total durasi:", total, "menit")
    print(f"Rata-rata durasi: {rata_rata:.2f} menit")
    print("Durasi terlama:", terlama, "menit")

    # Mengurutkan tanpa mengubah list asli
    urutan_durasi = sorted(durasi_peminjaman, reverse=True)

    print()
    print("Urutan durasi terlama:")

    for i in range(len(urutan_durasi)):
        print(f"{i + 1}. {urutan_durasi[i]} menit")

else:
    print("Belum ada data peminjaman")
