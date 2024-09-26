from tabulate import tabulate

# Daftar barang
barang = {
    1: {"nama": "Bayam", "harga": 5000},
    2: {"nama": "Terong", "harga": 4500},
    3: {"nama": "Kubis", "harga": 6000},
    4: {"nama": "Labu", "harga": 7000},
    5: {"nama": "Brokoli", "harga": 8000},
}

# Fungsi untuk menampilkan daftar barang
def tampilkan_daftar_barang():
    print("SELAMAT DATANG DI KASIR")
    tabel_data = [[kode, info['nama'], info['harga']] for kode, info in barang.items()]
    print(tabulate(tabel_data, headers=["Kode", "Nama Barang", "Harga"], tablefmt="grid"))

# Fungsi untuk menghitung total harga dan diskon
def hitung_total_harga_dan_diskon(total_harga):
    diskon = 0
    if 20000 <= total_harga <= 50000:
        diskon = 10
    elif 50000 < total_harga <= 100000:
        diskon = 15
    elif total_harga > 100000:
        diskon = 20
    
    total_diskon = total_harga * (diskon / 100)
    total_bayar = total_harga - total_diskon
    return diskon, total_diskon, total_bayar

# Fungsi utama untuk menjalankan program kasir
def main():
    tampilkan_daftar_barang()
    
    total_harga = 0
    jenis_barang = int(input("Berapa jenis barang yang akan dibeli? "))
    
    barang_beli = []
    
    for _ in range(jenis_barang):
        while True:
            try:
                kode_barang = int(input("Masukkan kode barang: "))
                if kode_barang not in barang:
                    raise ValueError
                break
            except ValueError:
                print("Kode barang tidak valid, silakan masukkan ulang.")
        
        jumlah_beli = int(input(f"Berapa banyak {barang[kode_barang]['nama']} yang akan dibeli? "))
        barang_beli.append([barang[kode_barang]['nama'], barang[kode_barang]['harga'], jumlah_beli, barang[kode_barang]['harga'] * jumlah_beli])
        total_harga += barang[kode_barang]['harga'] * jumlah_beli
    
    # Hitung diskon dan total bayar
    diskon, total_diskon, total_bayar = hitung_total_harga_dan_diskon(total_harga)
    
    # Tampilkan struk belanja
    print("\nSTRUK BELANJA")
    print(tabulate(barang_beli, headers=["Nama Barang", "Harga Satuan", "Jumlah", "Total Harga"], tablefmt="grid"))
    print(f"Total harga: Rp {total_harga}")
    if diskon > 0:
        print(f"Diskon {diskon}%: Rp {total_diskon}")
    else:
        print("Diskon: Tidak ada")
    print(f"Total yang harus dibayar: Rp {total_bayar}")
    print("Terima kasih telah berbelanja!")

if __name__ == "__main__":
    main()