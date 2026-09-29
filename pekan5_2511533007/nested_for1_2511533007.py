batas_3007 = int(input("Masukkan nilai batas: "))
for line_3007 in range(1, batas_3007 + 1):
    for j in range(1, (-1 * line_3007 + batas_3007) + 1):
        print(".", end="")
    print(line_3007)