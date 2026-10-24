from latihan4modul import hitungLuasSegitiga

# print("=== PROGRAM HITUNG LUAS SEGITIGA ===")
input_alas = float(input("Masukkan panjang alas (cm): "))
input_tinggi = float(input("Masukkan tinggi segitiga (cm): "))

hasil_luas = hitungLuasSegitiga(input_alas, input_tinggi)

print(f"Luas segitiga tersebut adalah: {hasil_luas} cm persegi")