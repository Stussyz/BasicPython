# Program Penentuan Prioritas Pelayanan Pasien

try:
    # Input data pasien
    nama = input("Masukkan nama pasien: ")
    umur = int(input("Masukkan umur pasien: "))
    suhu = float(input("Masukkan suhu tubuh pasien: "))
    tingkat_nyeri = int(input("Masukkan tingkat nyeri (0-10): "))
    status_darurat = input("Apakah pasien dalam kondisi darurat? (ya/tidak): ")

    # Mengubah input status darurat menjadi huruf kecil
    status_darurat = status_darurat.lower()

    # Struktur keputusan
    if status_darurat == "ya":
        kategori = "Prioritas 1 - Darurat"
        keterangan = "Pasien harus segera mendapat penanganan."

    else:
        if umur >= 60:
            if suhu >= 38 or tingkat_nyeri >= 7:
                kategori = "Prioritas 2 - Lansia dengan gejala serius"
                keterangan = "Pasien perlu mendapat pemeriksaan lebih cepat."
            else:
                kategori = "Prioritas 3 - Lansia stabil"
                keterangan = "Pasien tetap diprioritaskan karena termasuk lansia."

        else:
            if suhu >= 39 and tingkat_nyeri >= 7:
                kategori = "Prioritas 2 - Gejala serius"
                keterangan = "Pasien perlu mendapat pemeriksaan lebih cepat."
            elif suhu >= 38 or tingkat_nyeri >= 5:
                kategori = "Prioritas 3 - Perlu pemeriksaan"
                keterangan = "Pasien perlu diperiksa sesuai antrean prioritas."
            else:
                kategori = "Prioritas 4 - Umum"
                keterangan = "Pasien dapat mengikuti antrean umum."

    # Output hasil
    print()
    print("===== HASIL PRIORITAS PASIEN =====")
    print("Nama pasien:", nama)
    print("Kategori:", kategori)
    print("Keterangan:", keterangan)

except ValueError:
    print()
    print("Input umur, suhu tubuh, atau tingkat nyeri harus berupa angka.")
    print("Program dihentikan.")