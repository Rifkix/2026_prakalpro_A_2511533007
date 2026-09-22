#Program Menghitung Diskon Belanja

#input dari user
total_belanja_3007 = float(input("Masukkan total belanja (Rp): "))

#input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_3007 = input("Apakah Anda member(y/t): ").strip().lower()
is_member_3007 = input_member_3007 in ["y", "ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_3007 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_3007 = input_promo_3007 in ["y", "ya"]

total_diskon_persen_3007 = 0

# Multi IF terpisah: setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_3007 > 1000000:
    total_diskon_persen_3007 += 10 #diskon belanja besar

if is_member_3007:
    total_diskon_persen_3007 += 5 # diskon member

if kode_promo_valid_3007:
    total_diskon_persen_3007 += 15 # diskon voucher

# Menghitung nominal diskon dan total baya
nominal_diskon_3007 = total_belanja_3007 * (total_diskon_persen_3007/100)
total_bayar_3007 = total_belanja_3007 - nominal_diskon_3007

#Ouput hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total diskon : {total_diskon_persen_3007}% (Rp {nominal_diskon_3007:,.0f})")
print(f"Total bayar : Rp {total_bayar_3007:,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_3007}%")
#ouput: total diskon yang anda dapatkan: 30 jika belanja > 1 juta, member dan kode promo valid