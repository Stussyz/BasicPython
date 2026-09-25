#  break 1
# for nomor in range(1, 11):
#     if nomor == 4:
#         print("Nomor ditemukan")
#         break
#     print("Cek nomor", nomor)


# break 2
kode_dicari = "A03"

for nomor in range(1, 6):
    kode = input("Masukkan kode: ")

    if kode == kode_dicari:
        print("Kode ditemukan")
        break