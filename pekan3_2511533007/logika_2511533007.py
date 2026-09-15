# prorgam operator logika dalam python

# Memasukkan nilai boolean
# input tidak peka terhadap huruf besar dan kecil
a1_3007 = input("Input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2_3007 = input("Input nilai boolean-2 (True/False): ").strip().lower() == "true"

print("\nA1 =", a1_3007)
print("A2 =", a2_3007)

# Konjungsi : bernilai True jika keduanya True
hasil_3007 = a1_3007 and a2_3007
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_3007)

# Disjungsi : bernilai True jika salah satu True
hasil_3007 = a1_3007 or a2_3007
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_3007)

# Negasi A1: membalik nilai A1
hasil_3007 = not a1_3007
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_3007)

# Negasi A2: membalik nilai A2
hasil_3007 = not a2_3007
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_3007)

# XOR bernilai True jika kedua nilai berbeda
hasil_3007 = a1_3007 != a2_3007
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_3007)