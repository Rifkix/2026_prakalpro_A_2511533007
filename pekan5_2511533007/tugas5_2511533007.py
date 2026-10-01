print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
n_3007 = int(input("Masukkan ukuran skala jam pasir (N): "))

if n_3007 <= 0:
    print("N harus bilangan bulat positif")
else:
    # Border atas: # + (4N + 5) karakter "=" + #
    print("#", end="")
    for i_3007 in range(4 * n_3007 + 5):
        print("=", end="")
    print("#", end="")
    print()

    # Fase 1: jam pasir atas (baris N turun s.d. 1)
    for baris_3007 in range(n_3007, 0, -1):
        # Garis tegak kiri dan satu spasi padding
        print("|", end="")
        print(" ", end="")

        # Spasi penyeimbang kiri: 2 * (N - baris)
        for spasi_3007 in range(2 * (n_3007 - baris_3007)):
            print(" ", end="")

        # Deret angka mundur: baris turun ke 1, dipisahkan spasi
        for angka_3007 in range(baris_3007, 0, -1):
            print(angka_3007, end=" ")

        # Poros kristal
        print("<*>", end="")

        # Deret angka maju: 1 naik ke baris, diawali spasi
        for angka_3007 in range(1, baris_3007 + 1):
            print(" ", end="")
            print(angka_3007, end="")

        # Spasi penyeimbang kanan: 2 * (N - baris)
        for spasi_3007 in range(2 * (n_3007 - baris_3007)):
            print(" ", end="")

        # Satu spasi padding dan garis tegak kanan
        print(" ", end="")
        print("|", end="")
        print()

    # Fase 2: poros titik pusat
    print("|", end="")
    for spasi_3007 in range(2 * n_3007 + 1):
        print(" ", end="")
    print("<*>", end="")
    for spasi_3007 in range(2 * n_3007 + 1):
        print(" ", end="")
    print("|", end="")
    print()

    # Fase 3: jam pasir bawah (baris 1 naik s.d. N)
    for baris_3007 in range(1, n_3007 + 1):
        print("|", end="")
        print(" ", end="")

        for spasi_3007 in range(2 * (n_3007 - baris_3007)):
            print(" ", end="")

        for angka_3007 in range(baris_3007, 0, -1):
            print(angka_3007, end=" ")

        print("<*>", end="")

        for angka_3007 in range(1, baris_3007 + 1):
            print(" ", end="")
            print(angka_3007, end="")

        for spasi_3007 in range(2 * (n_3007 - baris_3007)):
            print(" ", end="")

        print(" ", end="")
        print("|", end="")
        print()

    # Border bawah
    print("#", end="")
    for i_3007 in range(4 * n_3007 + 5):
        print("=", end="")
    print("#", end="")
    print()