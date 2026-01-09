print("===================================")
print("     SISTEM PENJUALAN TIKET KAPAL   ")
print("===================================")


harga_tiket = {
    "Merak - Bakauheni": {
        "Ekonomi": 25000,
        "Bisnis": 40000
    },
    "Ternate - Sorong": {
        "Ekonomi": 250000,
        "Bisnis": 400000,
        "VIP": 600000
    }
}


print("\nDaftar Rute Kapal:")
for i, rute in enumerate(harga_tiket.keys(), start=1):
    print(f"{i}. {rute}")


pilih_rute = int(input("\nPilih rute (nomor): "))
rute_terpilih = list(harga_tiket.keys())[pilih_rute - 1]


print("\nKelas Tersedia:")
kelas_list = list(harga_tiket[rute_terpilih].keys())
for i, kelas in enumerate(kelas_list, start=1):
    print(f"{i}. {kelas}")


pilih_kelas = int(input("\nPilih kelas (nomor): "))
kelas_terpilih = kelas_list[pilih_kelas - 1]


jumlah = int(input("\nMasukkan jumlah tiket: "))


harga = harga_tiket[rute_terpilih][kelas_terpilih]
total = harga * jumlah


print("\n========= STRUK PEMBELIAN =========")
print("Rute          :", rute_terpilih)
print("Kelas         :", kelas_terpilih)
print("Harga Tiket   : Rp", harga)
print("Jumlah Tiket  :", jumlah)
print("Total Bayar   : Rp", total)
print("=================================")
print("Terima kasih telah membeli tiket!")