print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")


# 1. Input Data Pengunjung & String Handling
nama_3007 = input("Masukkan Nama Pengunjung        : ")
umur_3007 = int(input("Input umur anda                 : "))
sim_3007 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()[0]

# 2. Pemilihan Wahana menggunakan match-case
print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")
paket_3007 = int(input("Masukkan nomor paket (1-5)      : "))

nama_wahana_3007 = ""
harga_satuan_3007 = 0

match paket_3007:
    case 1:
        nama_wahana_3007 = "Wahana Safari Rimba"
        harga_satuan_3007 = 50000
    case 2:
        nama_wahana_3007 = "Wahana Arung Jeram"
        harga_satuan_3007 = 75000
    case 3:
        nama_wahana_3007 = "Wahana Motor ATV Ekstrim"
        harga_satuan_3007 = 120000
    case 4:
        nama_wahana_3007 = "Wahana Roller Coaster Kilat"
        harga_satuan_3007 = 100000
    case 5:
        nama_wahana_3007 = "Wahana All-Access VIP"
        harga_satuan_3007 = 220000
    case _:
        print("Paket wahana tidak valid!")
        exit()

jumlah_tiket_3007 = int(input("Masukkan jumlah tiket           : "))

if jumlah_tiket_3007 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")

input_member_3007 = input("Apakah Anda member? (y/t)       : ").strip().lower()
is_member_3007 = input_member_3007 in ["y", "ya"]

input_promo_3007 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()
kode_promo_valid_3007 = input_promo_3007 in ["y", "ya"]


# 3. Validasi Izin Kendali Wahana - if-elif-else + operator logika
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_3007 == 3 and umur_3007 >= 17 and sim_3007 == 'y':
    print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
elif paket_3007 == 3 and umur_3007 >= 17 and sim_3007 != 'y':
    print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
elif paket_3007 == 3 and umur_3007 < 17 and sim_3007 == 'y':
    print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
elif paket_3007 == 3 and umur_3007 < 17 and sim_3007 != 'y':
    print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
elif paket_3007 != 3 and umur_3007 >= 10:
    print("Status Akses: Anda memenuhi syarat umur untuk menikmati wahana ini.")
else:
    print("Status Akses: Anda belum cukup umur untuk menikmati wahana ini.")


# 4. Akumulasi Diskon Bertingkat - Multi-IF Terpisah
subtotal_3007 = harga_satuan_3007 * jumlah_tiket_3007
total_diskon_persen_3007 = 0

if subtotal_3007 >= 200000:
    total_diskon_persen_3007 += 10  # Diskon Belanja Besar

if is_member_3007:
    total_diskon_persen_3007 += 5  # Diskon Member

if kode_promo_valid_3007:
    total_diskon_persen_3007 += 15  # Diskon Voucher Promo

if jumlah_tiket_3007 >= 5:
    total_diskon_persen_3007 += 5  # Diskon Tambahan Rombongan

nominal_diskon_3007 = subtotal_3007 * (total_diskon_persen_3007 / 100)
total_bayar_3007 = subtotal_3007 - nominal_diskon_3007


# 5. Evaluasi Kelulusan Audit - if-else
if total_bayar_3007 > 300000:
    catatan_layanan_3007 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_3007 = "Terima kasih telah berkunjung."


print("\n--- Rincian Pembayaran ---")
print(f"Nama Pengunjung  : {nama_3007}")
print(f"Wahana Dipilih   : {nama_wahana_3007}")
print(f"Jumlah Tiket     : {jumlah_tiket_3007}")
print(f"Subtotal Belanja : Rp {subtotal_3007:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_3007}% (Rp {nominal_diskon_3007:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_3007:,.0f}")
print(f"Catatan Layanan  : {catatan_layanan_3007}")
print("Program Selesai")