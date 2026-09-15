print("\n=====================================")
print("3. OPERATOR BITWISE")
print("=====================================")

angka1_3007 = int(input("Input angka bitwise-1: "))
angka2_3007 = int(input("Input angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1_3007, "| biner =", bin(angka1_3007))
print("angka2 =", angka2_3007, "| biner =", bin(angka2_3007))

# Bitwise AND
hasil_3007 = angka1_3007 & angka2_3007
print("\nOperator Bitwise AND (&)")
print(angka1_3007, "&", angka2_3007, "=", hasil_3007)
print("Biner hasil =", bin(hasil_3007))
print("Biner hasil (8 bit) =", format(hasil_3007, '08b'))

# Bitwise OR
hasil_3007 = angka1_3007 | angka2_3007
print("\nBitwise OR (|)")
print(angka1_3007, "|", angka2_3007, "=", hasil_3007)
print("Biner hasil =", bin(hasil_3007))
print("Biner hasil (8 bit) =", format(hasil_3007, '08b'))

# Bitwise XOR
hasil_3007 = angka1_3007 ^ angka2_3007
print("\nBitwise XOR (^)")
print(angka1_3007, "^", angka2_3007, "=", hasil_3007)
print("Biner hasil =", bin(hasil_3007))
print("Biner hasil (8 bit) =", format(hasil_3007, '08b'))

# Bitwise NOT
hasil_3007 = ~angka1_3007
print("\nBitwise NOT (~)")
print("~", angka1_3007, "=", hasil_3007)
print("Biner hasil =", bin(hasil_3007))
print("Biner hasil (8 bit) =", format(hasil_3007, '08b'))

# Bitwise geser kiri
jumlah_geser_3007 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_3007 = angka1_3007 << jumlah_geser_3007
print("\nBitwise Geser Kiri (<<)")
print(angka1_3007, "<<", jumlah_geser_3007, "=", hasil_3007)
print("Biner hasil =", bin(hasil_3007))
print("Biner hasil (8 bit) =", format(hasil_3007, '08b'))

# Bitwise geser kanan
hasil_3007 = angka1_3007 >> jumlah_geser_3007
print("\nBitwise Geser Kanan (>>)")
print(angka1_3007, ">>", jumlah_geser_3007, "=", hasil_3007)
print("Biner hasil =", bin(hasil_3007))
print("Biner hasil (8 bit) =", format(hasil_3007, '08b'))