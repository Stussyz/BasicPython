# SISTEM PELAYANAN PASIEN PRIORITAS
print("=== SISTEM PELAYANAN PASIEN RUMAH SAKIT ===")

# INPUT DATA PASIEN
nama = input("Nama pasien               : ")
umur = int(input("Umur pasien               : "))

status_darurat = input("Status darurat (ya/tidak)  : ").lower()
status_hamil = input("Status ibu hamil (ya/tidak): ").lower()
status_disabilitas = input("Disabilitas (ya/tidak)      : ").lower()
status_registrasi = input("Registrasi (lengkap/tidak)  : ").lower()
status_jadwal = input("Memiliki jadwal (ya/tidak)  : ").lower()

# MENGUBAH INPUT MENJADI NILAI BOOLEAN
darurat = status_darurat == "ya"
hamil = status_hamil == "ya"
disabilitas = status_disabilitas == "ya"
registrasi_lengkap = status_registrasi == "lengkap"
ada_jadwal = status_jadwal == "ya"

# Kondisi prioritas khusus
prioritas_khusus = umur >= 60 or hamil or disabilitas

# PROSES PENENTUAN PRIORITAS
if darurat:
    kategori = "PRIORITAS 1 - Pelayanan Darurat"
    keterangan = "Pasien harus segera mendapatkan pelayanan darurat."

elif not registrasi_lengkap:
    kategori = "REGISTRASI BELUM LENGKAP"
    keterangan = "Silakan melengkapi data registrasi terlebih dahulu."

elif registrasi_lengkap and prioritas_khusus:
    kategori = "PRIORITAS 2 - Jalur Pelayanan Prioritas"

    # Nested if
    if umur >= 70 or disabilitas:
        keterangan = (
            "Pasien membutuhkan bantuan petugas "
            "selama proses pelayanan."
        )
    else:
        keterangan = (
            "Pasien dapat menunggu pada "
            "jalur pelayanan prioritas."
        )

elif registrasi_lengkap and not prioritas_khusus and ada_jadwal:
    kategori = "PRIORITAS 3 - Pasien Terjadwal"
    keterangan = "Pasien dapat mengikuti antrean sesuai jadwal pemeriksaan."

else:
    kategori = "PRIORITAS 4 - Antrean Reguler"
    keterangan = "Pasien mengikuti antrean pelayanan reguler."

# OUTPUT
print()
print("===== HASIL PELAYANAN PASIEN =====")
print("Nama Pasien      :", nama)
print("Umur             :", umur, "tahun")
print("Status Darurat   :", status_darurat)
print("Status Registrasi:", status_registrasi)
print()
print("Kategori         :", kategori)
print("Keterangan       :", keterangan)