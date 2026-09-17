from typing import Final

BATAS_LULUS_3007: Final = 90.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_3007 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_3007 = input("Masukkan Jenis Kelamin (L/P): ")
umur_3007 = int(input("Masukkan Umur            : "))
skor_tes_awal_3007 = float(input("Masukkan Skor Tes Awal   : "))

alamat_3007 = """Jl. Koto Tangah,
Kecamatan Pauh,
Kota Padang,
Provinsi Sumatera Barat"""

id_token_sinyal_3007 = 100 + 3j

status_kelulusan_3007 = skor_tes_awal_3007 >= BATAS_LULUS_3007

print()
print("=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa :", nama_3007, "| Tipe:", type(nama_3007))
print("Jenis Kelamin  :", jenis_kelamin_3007, "| Tipe:", type(jenis_kelamin_3007))
print("Alamat Domisili:")
print(alamat_3007, "| Tipe:", type(alamat_3007))
print("Umur           :", umur_3007, "tahun | Tipe:", type(umur_3007))
print("Skor Tes Awal  :", skor_tes_awal_3007, "| Tipe:", type(skor_tes_awal_3007))
print("ID Token Sinyal:", id_token_sinyal_3007, "| Tipe:", type(id_token_sinyal_3007))

print()
print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai:", BATAS_LULUS_3007)
print("Apakah Dinyatakan Lulus?:", status_kelulusan_3007, "| Tipe:", type(status_kelulusan_3007))