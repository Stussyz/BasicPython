# for nomor in range(1, 6):
#     if nomor == 3:
#         continue
#     print("Proses nomor", nomor)
    
    
# continue 2
for sesi in range(1, 6):
    status = input("Status sesi " + str(sesi) + ": ")

    if status == "libur":
        continue

    print("Sesi", sesi, "diproses")