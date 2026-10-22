print("=== SISTEM REKAP PELAYANAN HELPDESK IT ===")

# Memasukkan jumlah target tiket
jumlah_tiket = int(input("Masukkan jumlah tiket pada sesi ini: "))

# Validasi jumlah tiket menggunakan while
while jumlah_tiket <= 0:
    print("Jumlah tiket harus lebih dari 0.")
    jumlah_tiket = int(input("Masukkan jumlah tiket pada sesi ini: "))


# Variabel awal untuk rekap
default_tiketDiproses = 0
default_tiketSelesai = 0
default_tiketPending = 0
tiket_prioritas = 0
total_waktu = 0

sisa_tiket = jumlah_tiket


# Memeriksa tiket satu per satu
for nomor in range(1, jumlah_tiket + 1):

    print()
    print("===== TIKET", nomor, "=====")

    id_tiket = input("ID tiket        : ")

    # Menghentikan proses lebih awal
    if id_tiket.upper() == "STOP":
        print("Proses pemeriksaan tiket dihentikan oleh petugas.")
        break

    nama_pelapor = input("Nama pelapor    : ")
    jenis_laporan = input("Jenis laporan   : ")
    prioritas = input("Prioritas (normal/prioritas): ").lower()

    lama_penanganan = int(
        input("Lama penanganan dalam menit: ")
    )

    hasil = input(
        "Hasil penanganan (selesai/pending): "
    ).lower()


    # Tiket ini sudah diperiksa,
    # sehingga sisa tiket berkurang
    sisa_tiket -= 1


    # Memeriksa validitas lama penanganan
    if lama_penanganan <= 0:
        print("Data tiket tidak valid. Tiket dilewati.")
        print("Sisa tiket yang belum diperiksa:", sisa_tiket)
        continue


    # Tiket valid berhasil diproses
    tiket_diproses += 1
    total_waktu += lama_penanganan


    # Menghitung hasil penanganan
    if hasil == "selesai":
        tiket_selesai += 1

    elif hasil == "pending":
        tiket_pending += 1


    # Menghitung tiket prioritas
    if prioritas == "prioritas":
        tiket_prioritas += 1


    print("Tiket berhasil diproses.")
    print("Sisa tiket yang belum diperiksa:", sisa_tiket)


# Dijalankan jika for selesai tanpa break
else:
    print()
    print("Seluruh target tiket pada sesi ini telah diperiksa.")


# Menghitung rata-rata waktu penanganan
if tiket_diproses > 0:
    rata_rata = total_waktu / tiket_diproses
else:
    rata_rata = 0


# Menampilkan rekap akhir
print()
print("=====================================")
print("       REKAP LAYANAN HELPDESK")
print("=====================================")

print("Target tiket             :", jumlah_tiket)
print("Tiket berhasil diproses  :", tiket_diproses)
print("Tiket selesai            :", tiket_selesai)
print("Tiket pending            :", tiket_pending)
print("Tiket prioritas          :", tiket_prioritas)
print("Total waktu              :", total_waktu, "menit")
print("Rata-rata penanganan     :", rata_rata, "menit")
print("Sisa tiket belum diperiksa:", sisa_tiket)