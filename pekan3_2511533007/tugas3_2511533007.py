# === SISTEM SIMULASI TRANSAKSI DAN VALIDASI AKSES TOKO ===

# 1. INPUT DATA (Menerima input dari pengguna)
print("=== SISTEM TRANSAKSI TOKO ===\n")
nama_3007 = input("Masukkan Nama Pelanggan : ")
status_3007 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()
total_belanja_3007 = int(input("Masukkan Total Belanja : "))
jumlah_barang_3007 = int(input("Masukkan Jumlah Barang : "))
kode_promo_3007 = input("Masukkan Kode Promo : ").upper()

print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan       : {nama_3007}")
print(f"Status Pelanggan     : {status_3007}")
print(f"Total Belanja        : Rp{total_belanja_3007}")
print(f"Jumlah Barang        : {jumlah_barang_3007}")
print(f"Kode Promo           : {kode_promo_3007}")

# 2. OPERATOR PERBANDINGAN & KEANGGOTAAN
daftar_promo_3007 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]
cek_belanja_3007 = total_belanja_3007 >= 200000    # Operator >=
cek_barang_3007 = jumlah_barang_3007 >= 3          # Operator >=
cek_member_3007 = status_3007 == "member"          # Operator ==
promo_tersedia_3007 = kode_promo_3007 in daftar_promo_3007 # Operator IN

# 3. OPERATOR LOGIKA
# Diskon didapat jika member AND belanja minimum tercapai
dapat_diskon_3007 = cek_member_3007 and cek_belanja_3007
# Promo didapat jika kode valid AND (barang cukup OR sudah dapat diskon)
dapat_promo_3007 = promo_tersedia_3007 and (cek_barang_3007 or dapat_diskon_3007)
# Contoh penggunaan operator not
bukan_member_3007 = not cek_member_3007

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000        : {cek_belanja_3007}")
print(f"Jumlah Barang >= 3         : {cek_barang_3007}")
print(f"Status Member              : {cek_member_3007}")
print(f"Kode Promo Tersedia        : {promo_tersedia_3007}")
print(f"Mendapatkan Diskon         : {dapat_diskon_3007}")
print(f"Mendapatkan Promo          : {dapat_promo_3007}")

# 4. OPERATOR ARITMATIKA & PENUGASAN (AUGMENTED ASSIGNMENT)
diskon_3007 = 0
if dapat_diskon_3007:
    diskon_3007 = total_belanja_3007 * 0.10  # Operator * (Perkalian)

total_bayar_3007 = total_belanja_3007
total_bayar_3007 -= diskon_3007              # Operator Penugasan -=

# Operator / (Pembagian) dan % (Modulus/Sisa Bagi)
rata_rata_3007 = total_bayar_3007 / jumlah_barang_3007 if jumlah_barang_3007 > 0 else 0
sisa_bagi_3007 = int(total_bayar_3007) % jumlah_barang_3007 

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                     : Rp{int(diskon_3007)}")
print(f"Total Pembayaran           : Rp{int(total_bayar_3007)}")
print(f"Rata-rata Harga Barang     : Rp{int(rata_rata_3007)}")

# 5. OPERATOR BITWISE
# Representasi bit: Member(0001), Belanja(0010), Barang(0100), Promo(1000)
bit_member_3007 = 1 if cek_member_3007 else 0       
bit_belanja_3007 = 2 if cek_belanja_3007 else 0     
bit_barang_3007 = 4 if cek_barang_3007 else 0       
bit_promo_3007 = 8 if promo_tersedia_3007 else 0    

# OR (|) untuk menggabungkan kondisi
status_transaksi_3007 = bit_member_3007 | bit_belanja_3007 | bit_barang_3007 | bit_promo_3007

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Kode Hak Akses             : {format(status_transaksi_3007, '04b')}")
# AND (&) untuk mengekstrak/memeriksa hak akses
print(f"Member Access              : {(status_transaksi_3007 & 1) > 0}")
print(f"Promo Access               : {(status_transaksi_3007 & 8) > 0}")
print(f"Free Shipping Access       : {(status_transaksi_3007 & 4) > 0}")

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print("0001 | 0010 | 0100 | 1000")
print(f"Kode Biner   : {format(status_transaksi_3007, '04b')}")
print(f"Kode Desimal : {status_transaksi_3007}")

print("=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{format(status_transaksi_3007, '04b')} & 0001")
cek_bit_member_3007 = status_transaksi_3007 & 1
print(f"Hasil Biner   : {format(cek_bit_member_3007, '04b')}")
print(f"Hasil Desimal : {cek_bit_member_3007}")

print("\nCek Promo")
print(f"{format(status_transaksi_3007, '04b')} & 1000")
cek_bit_promo_3007 = status_transaksi_3007 & 8
print(f"Hasil Biner   : {format(cek_bit_promo_3007, '04b')}")
print(f"Hasil Desimal : {cek_bit_promo_3007}")

print("=== Perbandingan Status ===")
# Misal membandingkan dengan profil target (1011 = Member, Belanja>=200k, Promo valid)
kode_referensi_3007 = 11 
print(f"Kode Transaksi : {format(status_transaksi_3007, '04b')}")
print(f"Kode Referensi : {format(kode_referensi_3007, '04b')}")
print(f"{format(status_transaksi_3007, '04b')} ^ {format(kode_referensi_3007, '04b')}")
hasil_xor_3007 = status_transaksi_3007 ^ kode_referensi_3007
print(f"Hasil Biner   : {format(hasil_xor_3007, '04b')}")
print(f"Hasil Desimal : {hasil_xor_3007}")

print("=== Shift ===")
print(f"{format(status_transaksi_3007, '04b')} << 1")
hasil_shift_3007 = status_transaksi_3007 << 1
print(f"Hasil Biner   : {format(hasil_shift_3007, '05b')}")
print(f"Hasil Desimal : {hasil_shift_3007}")

# 6. OPERATOR IDENTITAS (Tambahan Bukti Operasi)
print("\n=== DEMONSTRASI OPERATOR IDENTITAS ===")
objek1_3007 = daftar_promo_3007
objek2_3007 = objek1_3007
objek3_3007 = daftar_promo_3007.copy()

print(f"objek1 is objek2      = {objek1_3007 is objek2_3007}")
print(f"objek1 is not objek3  = {objek1_3007 is not objek3_3007}")
print(f"objek1 == objek3      = {objek1_3007 == objek3_3007} (Isi sama, namun identitas di memori berbeda)")

print("\n=== SELESAI ===")