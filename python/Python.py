# Fungsi untuk menghitung luas trapesium
def hitung_luas_trapesium(sisi_atas, sisi_bawah, tinggi):
    luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
    return luas

# Menetapkan nilai sisi atas, sisi bawah, dan tinggi secara langsung
sisi_atas = 1.0  # Misalnya 10.0
sisi_bawah = 1.0  # Misalnya 15.0
tinggi = 7.0  # Misalnya 7.0

# Menghitung luas trapesium
luas = hitung_luas_trapesium(sisi_atas, sisi_bawah, tinggi)

# Menampilkan hasil perhitungan
print("Luas trapesium adalah:", luas)
