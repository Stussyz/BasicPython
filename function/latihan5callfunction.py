import latihan4modul2
from garis import garisBukaTutup
inputLuas = int(input("Masukkan Sisi yang Anda Inginkan: "))

hasil_luas = latihan4modul2.hitungLPersegi(inputLuas)
garisBukaTutup()
print(f"Luas persegi tersebut adalah: {hasil_luas} cm persegi")