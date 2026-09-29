tinggi_3007 = int(input("Masukkan tinggi pola (bilangan genap, misalnya 10): "))

if tinggi_3007 % 2 != 0:
    print("Tinggi harus bilangan genap")
else:
    a_3007 = tinggi_3007
    c_3007 = a_3007
    lebar_3007 = (2 * tinggi_3007) - 2

    for i_3007 in range(1, tinggi_3007 + 1):
        b_3007 = c_3007 + 1

        for j_3007 in range(1, lebar_3007 + 1):

            #Baris atas dan bawah
            if i_3007 == 1 or i_3007 == tinggi_3007:
                if j_3007 == 1 or j_3007 == lebar_3007:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris isi
            else:
                if j_3007 == 1 or j_3007 == lebar_3007:
                    print("|", end="")
                else:
                    if j_3007 == c_3007:
                        print("<", end="")
                    elif j_3007 == b_3007:
                        print(">", end="")
                    elif j_3007 == (lebar_3007 - c_3007):
                        print("<", end="")
                    elif j_3007 == (lebar_3007 - c_3007 + 1):
                        print(">", end="")
                    elif j_3007 > b_3007 and j_3007 < (lebar_3007 - c_3007):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli Java
        a_3007 -= 2

        if a_3007 <= 0:
            c_3007 = (-a_3007) + 2
        else:
            c_3007 = a_3007 
                    

