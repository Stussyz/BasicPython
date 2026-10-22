
# SOAL 1 - INVENTARIS LABORATORIUM

# Membuat list inventaris awal
inventaris = ["Flashdisk", "Mouse", "Kabel HDMI", "Adaptor"]

# Menampilkan daftar awal
print("===== INVENTARIS LABORATORIUM =====")
print()
print("Inventaris Awal:")
print(inventaris)

# Mengubah nama peralatan menggunakan indeks
inventaris[1] = "Mouse Wireless"

# Menambahkan peralatan baru
inventaris.append("Proyektor")

# Menghapus peralatan
inventaris.remove("Adaptor")

# Menampilkan informasi inventaris
print()
print("===== HASIL PEMBARUAN =====")
print("Jumlah peralatan:", len(inventaris))
print("Peralatan pertama:", inventaris[0])
print("Peralatan terakhir:", inventaris[-1])

# Mengurutkan inventaris berdasarkan abjad
inventaris.sort()

# Menampilkan daftar dengan nomor urut
print()
print("Daftar Inventaris Terbaru:")

for i in range(len(inventaris)):
    print(f"{i + 1}. {inventaris[i]}")
