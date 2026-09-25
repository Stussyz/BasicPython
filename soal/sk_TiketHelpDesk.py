print("=== SISTEM REKAP LAYANAN HELPDESK ===")

jumlah_tiket = int(input("Masukkan jumlah tiket yang akan diproses: "))

# Validasi jumlah tiket menggunakan while
while jumlah_tiket <= 0:
    print("Jumlah tiket harus lebih dari 0.")
    jumlah_tiket = int(input("Masukkan jumlah tiket yang akan diproses: "))

# Variabel penghitung
tiket_diproses = 0
tiket_selesai = 0
tiket_pending = 0
tiket_prioritas = 0
total_waktu = 0
sisa_tiket = jumlah_tiket

# Perulangan utama
for nomor in range(1, jumlah_tiket + 1):

    print()
    print("===== TIKET", nomor, "=====")

    id_tiket = input("ID tiket        : ")

    # Menghentikan perulangan
    if id_tiket.upper() == "STOP":
        print("Proses input tiket dihentikan oleh petugas.")
        break

    nama = input("Nama pelapor    : ")
    status = input("Status tiket (selesai/pending): ").lower()
    prioritas = input("Prioritas (normal/prioritas): ").lower()
    lama = int(input("Lama penanganan : "))

    # Data tidak valid
    if lama <= 0:
        print("Data tiket tidak valid. Tiket dilewati.")
        continue

    # Tiket valid
    tiket_diproses += 1
    total_waktu += lama

    # Decrement
    sisa_tiket -= 1

    # Menghitung status tiket
    if status == "selesai":
        tiket_selesai += 1
    elif status == "pending":
        tiket_pending += 1

    # Menghitung tiket prioritas
    if prioritas == "prioritas":
        tiket_prioritas += 1

    print("Tiket berhasil diproses.")
    print("Sisa tiket:", sisa_tiket)

# Dijalankan jika for selesai tanpa break
else:
    print()
    print("Seluruh target tiket telah selesai diproses.")


# Menghitung rata-rata
if tiket_diproses > 0:
    rata_rata = total_waktu / tiket_diproses
else:
    rata_rata = 0


# Rekap
print()
print("================================")
print("     REKAP LAYANAN HELPDESK")
print("================================")

print("Target tiket         :", jumlah_tiket)
print("Tiket diproses       :", tiket_diproses)
print("Tiket selesai        :", tiket_selesai)
print("Tiket pending        :", tiket_pending)
print("Tiket prioritas      :", tiket_prioritas)
print("Total waktu          :", total_waktu, "menit")
print("Sisa tiket           :", sisa_tiket)
print("Rata-rata penanganan :", rata_rata, "menit")