blocked_seat = int(input("Masukkan blocked seat: "))

for row in range(1, 4):
    print("Row", row, end=": ")
    for kursi in range(1, 6):
        if kursi == blocked_seat:
            break
        print(kursi, end=" ")
    print()
