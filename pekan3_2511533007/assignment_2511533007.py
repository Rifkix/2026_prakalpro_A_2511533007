# Program operator assignment dalam python

angka1_3007 = int(input("Input angka-1: "))
angka2_3007 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_3007)
print("Nilai angka2 =", angka2_3007)

# assignment biasa
hasil_3007 = angka1_3007
print("\nAssignment Biasa (=)")
print("Hasil =", hasil_3007)

# assignment penambahan
hasil_3007 = angka1_3007
hasil_3007 += angka2_3007
print("\nAssignment Penambahan (+=)")
print("Hasil =", hasil_3007)

# assignment pengurangan
hasil_3007 = angka1_3007
hasil_3007 -= angka2_3007
print("\nAssignment Pengurangan (-=)")
print("Hasil =", hasil_3007)

# assignment perkalian
hasil_3007 = angka1_3007
hasil_3007 *= angka2_3007
print("\nAssignment Perkalian (*=)")
print("Hasil =", hasil_3007)

# assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3007 != 0:
    hasil_3007 = angka1_3007
    hasil_3007 /= angka2_3007
    print("\nAssignment Pembagian (/=)")
    print("Hasil =", hasil_3007)
    #Operator tambahan
    hasil_3007 = angka1_3007
    hasil_3007 //= angka2_3007
    print("\nAssignment Pembagian Bulat (//=)")
    print("Hasil =", hasil_3007)
    hasil_3007 = angka1_3007
    hasil_3007 %= angka2_3007
    print("\nAssignment Sisa Bagi (%=)")
    print("Hasil =", hasil_3007)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil = angka1_3007
hasil **= angka2_3007
print("\nAssignment Perpangkatan (**=)")
print("Hasil =", hasil)
