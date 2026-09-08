is_lulus_3007 = True
is_cumlaude_3007 = False

#menggunakan Boolean
nilai_3007 = 85
batas_lulus_3007 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan_3007 = nilai_3007 >= batas_lulus_3007 # Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai:", nilai_3007)
print("Apakah Lulus?:", status_kelulusan_3007)
if is_lulus_3007 and is_cumlaude_3007:
    print("Selamat, Anda lulus dengan predikat cumlaude!")