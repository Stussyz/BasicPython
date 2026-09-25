# # tanpa looping
# print("antrean 1")
# print("antrean 2")
# print("antrean 3")
# print("antrean 4")
# print("antrean 5")
# print("===BATAS AKHIR TANPA LOOP===")

# # dengan looping
# for nomor in range (1, 6):
#     print("Antrean", nomor)
# print("===BATAS AKHIR DENGAN LOOP===")
    
# # membuat pola segitiga siku dengan *
# tinggi = 5
# # range (mulai, sampai, step)
# for a in range(1, tinggi + 1):
#     print("*" * a)
# print("===BATAS AKHIR POLA SEGITIGA===")

# # membuat pola piramida
# tinggi = 5

# for b in range(tinggi):
#     spasi = " " * (tinggi - b - 1)
#     bintang = "*" * (2 * b + 1)
#     print(spasi + bintang)
# print("===BATAS AKHIR POLA PIRAMIDA===")


# menenetukan bilangan ganjil dan genap
batas = int(input("Cek angka sampai: "))
for angka in range(1, batas + 1):
    if angka % 2 == 0:
        print(angka, "genap")
    else:
        print(angka, "ganjil")