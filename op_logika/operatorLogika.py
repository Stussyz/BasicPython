# Logika AND
status = input("Status aktif? (ya/tidak): ")
kartu = input("Membawa kartu? (ya/tidak): ")

if status == "ya" and kartu == "ya":
    print("Akses diberikan.")
else:
    print("Akses ditolak.")


# Logika OR
terdaftar = input("Terdaftar praktikum? (ya/tidak): ")
izin_dosen = input("Ada izin dosen? (ya/tidak): ")

if terdaftar == "ya" or izin_dosen == "ya":
    print("Boleh memakai laboratorium.")
else:
    print("Belum boleh memakai laboratorium.")

# Logika NOT
maintenance = input("Lab maintenance? (ya/tidak): ") == "ya"

if not maintenance:
    print("Lab dapat digunakan.")
else:
    print("Lab sedang tidak dapat digunakan.")
