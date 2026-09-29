ulang_3007 = int(input("Masukkan jumlah perulangan: "))

jumlah_3007 = 0
for i_3007 in range(1, ulang_3007 + 1):
    print(i_3007, end=" ")
    jumlah_3007 = jumlah_3007 + i_3007

    if i_3007 < ulang_3007:
        print(" + ", end=" ")
    else:
        print(" = ", jumlah_3007, end=" ")
print()
print("Jumlah =", jumlah_3007)
