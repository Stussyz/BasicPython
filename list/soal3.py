
# SOAL 3 - RESERVASI KURSI BIOSKOP

# Nested list untuk status kursi
# 0 = Tersedia
# 1 = Sudah dipesan

kursi = [
    [1, 0, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 0]
]

print("===== SISTEM RESERVASI BIOSKOP =====")
print()
print("Kondisi Kursi Awal:")

# Menampilkan kursi menggunakan nested loop
for i in range(len(kursi)):
    print(f"Baris {i + 1}:", end=" ")

    for j in range(len(kursi[i])):
        print(kursi[i][j], end=" ")

    print()

# Input nomor kursi
print()
baris = int(input("Masukkan nomor baris (1-3): "))
kolom = int(input("Masukkan nomor kursi (1-4): "))

# Mengubah nomor pengguna menjadi indeks
indeks_baris = baris - 1
indeks_kolom = kolom - 1

# Mengecek validitas nomor kursi
if baris < 1 or baris > 3 or kolom < 1 or kolom > 4:
    print()
    print("Nomor kursi tidak valid")

# Mengecek kursi yang sudah dipesan
elif kursi[indeks_baris][indeks_kolom] == 1:
    print()
    print("Kursi sudah dipesan")

# Melakukan pemesanan
else:
    kursi[indeks_baris][indeks_kolom] = 1
    print()
    print("Pemesanan berhasil!")

# Menampilkan kondisi terbaru
print()
print("===== KONDISI KURSI TERBARU =====")

for i in range(len(kursi)):
    print(f"Baris {i + 1}:", end=" ")

    for j in range(len(kursi[i])):
        print(kursi[i][j], end=" ")

    print()

# Menghitung total kursi
total_dipesan = 0
total_tersedia = 0

print()
print("===== REKAP KETERSEDIAAN =====")

# Nested loop untuk menghitung kursi
for i in range(len(kursi)):
    tersedia_per_baris = 0

    for j in range(len(kursi[i])):

        if kursi[i][j] == 0:
            tersedia_per_baris += 1
            total_tersedia += 1

        else:
            total_dipesan += 1

    print(f"Baris {i + 1}: {tersedia_per_baris} kursi tersedia")

# Menampilkan total keseluruhan
print()
print("Total kursi dipesan:", total_dipesan)
print("Total kursi tersedia:", total_tersedia)