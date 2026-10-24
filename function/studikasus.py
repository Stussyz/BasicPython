TARIF_PAJAK = 0.10  


def hitung_pajak_karyawan(gaji):
    """Menghitung potongan pajak dari gaji karyawan menggunakan tarif global"""
    return gaji * TARIF_PAJAK

def hitung_pajak_stnk(nilai_jual_motor):
    """Menghitung pajak tahunan STNK motor menggunakan tarif global"""
    return nilai_jual_motor * TARIF_PAJAK


print("=== 1. PERHITUNGAN PAJAK KARYAWAN ===")
gaji_pokok = 5000000
pajak_gaji = hitung_pajak_karyawan(gaji_pokok)
print(f"Gaji Pokok   : Rp{gaji_pokok:,.0f}")
print(f"Potongan PPh : Rp{pajak_gaji:,.0f}")

print("\n=== 2. PERHITUNGAN PAJAK STNK MOTOR ===")
harga_motor = 25000000
pajak_stnk = hitung_pajak_stnk(harga_motor)
print(f"Nilai Jual Motor : Rp{harga_motor:,.0f}")
print(f"Pajak STNK       : Rp{pajak_stnk:,.0f}")
