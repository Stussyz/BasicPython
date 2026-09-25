# # pemadanan karakter
# kode_kelas = "SI-B"
# isTrue = kode_kelas == "SI-B"
# print(isTrue)


# # pengecekan nilai
# nilai = 74
# kkm = 80
# cek_nilai = nilai >= kkm
# print(cek_nilai)



# pencocokan nilai ujian
# nilai_kkm = 75
# if nilai_kkm != 75:
#     print("nilai anda belum memenuhi kkm")
# else:
#     print("Nilai anda memenuhi kkm")
status_wni = input("Apakah anda WNI? (WNI/WNA): ")
if status_wni.upper()!= "WNI":
    print("Anda bukan WNI, anda tidak dapat mengakses layanan PEMILU!")
    isWNA = status_wni != "WNI"
    print(f"status WNA: {isWNA}")
else:
    print("Selamat datang, anda dapat mengakses layanan PEMILU!")
    
        
# persentase kehadiran
# jumlah_pertemuan = int(input("Masukkan jumlah pertemuan kelas (1 semester): "))
# jumlah_hadir = int(input("Masukkan jumlah kehadiran anda: "))
# persentase = (jumlah_hadir/jumlah_pertemuan) * 100

# if persentase >= 75:
#     print(f"Persentase kehadiran anda adalah {persentase:.2f}% anda memenuhi syarat sempro")
# else:
#     print(f"Persentase kehadiran anda adalah {persentase:.2f}% anda tidak memenuhi syarat sempro")
    

# # menentukan kondisi jalan
# jalan_rusak = input("Apakah jalan rusak? (ya/tidak): ")

# if jalan_rusak.lower() == "ya":
#     print("cari jalan alternatif!")
# else:
#     print("jalan dalam kondisi baik, selamat jalan")
    
    
# # password akses wifi
# iniPassword = input("Masukkan Password WiFi: ")

# if iniPassword == "UverS2026":
#     print("Akses WiFi diberikan.")
# else:
#     print("Password salah. Akses ditolak.")
    

# # if elif else dengan operator perbandingan
# nilai = 89

# if nilai >= 90:
#     print("Hebat! Anda dapat nilai A")
# elif nilai >= 80:
#     print("Bagus! Anda dapat nilai B")
# elif nilai >= 70:
#     print("Cukup. Anda dapat nilai C")
# else:
#     print("Maaf, Anda harus ikut remedial")
    

# # nested if dengan operator perbandingan
# umur = 18
# lulus_ujian = True

# if umur >= 17:
#     print("1. Syarat umur terpenuhi. Anda berhak mengikuti ujian.")
    
#     if lulus_ujian == True:
#         print("2. Selamat! Anda lulus ujian. SIM Anda segera dicetak.")
#     else:
#         print("2. Anda belum lulus ujian. Silakan coba lagi minggu depan.")

# else:
#     print("Mohon maaf, umur Anda belum mencukupi. Anda tidak bisa mendaftar SIM.")