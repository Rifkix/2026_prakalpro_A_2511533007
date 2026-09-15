#program ini menggunakan fungsi input()
#nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_3007 = int(input("Input angka-1: "))
angka2_3007 = int(input("Input angka-2: "))

#penjumlahan
hasil_3007 = angka1_3007 + angka2_3007
print("\nOperator Penjumlahan")
print("Hasil =", hasil_3007)

#pengurangan
hasil_3007 = angka1_3007 - angka2_3007
print("\nOperator Pengurangan")
print("Hasil =", hasil_3007)

#perkalian
hasil_3007 = angka1_3007 * angka2_3007
print("\nOperator Perkalian")
print("Hasil =", hasil_3007)

#pembagian, pembagian bulat, dan sisa bagi
if angka1_3007 != 0:
    hasil_3007 = angka1_3007 / angka2_3007
    print("\nOperator Pembagian")
    print("Hasil =", hasil_3007)

    hasil_3007 = angka1_3007 // angka2_3007
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_3007)

    hasil_3007 = angka1_3007 % angka2_3007
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_3007)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# pangkat
hasil_3007 = angka1_3007 ** angka2_3007
print("\nOperator pangkat")
print("Hasil =", hasil_3007)
