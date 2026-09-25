# input
nama_barang = input("masukkan nama barang: ")
harga_barang = float(input("masukkan harga barang: "))
jumlah_barang = int(input("masukkan jumlah barang: "))

# process
subtotal = harga_barang * jumlah_barang
diskon = subtotal * 0.10
total = subtotal - diskon

# output
print("\nMinimarket")
print(f"nama barang: {nama_barang}")
print(f"subtotal: Rp{subtotal:,.2f}")
print(f"diskon : Rp{diskon:,.2f}")
print(f"total pembayaran: Rp{total:,.2f}")