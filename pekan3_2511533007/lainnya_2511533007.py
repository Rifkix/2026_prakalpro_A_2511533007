#Program operator keanggotaan dan identitas

print("=====================================")
print("1. OPERATOR KEANGGOTAAN")
print("=====================================")

#input beberapa data yang dipisahkan dengan koma
input_data_3007 = input("Masukkan beberapa angka, pisahkan dengan koma:")

#mengubah input menjadi list integer
data_3007 = [int(angka_3007.strip()) for angka_3007 in input_data_3007.split(",")]

nilai_dicari_3007 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_3007 = nilai_dicari_3007 in data_3007
print("\nOperator keanggotaan IN")
print("Apakah", nilai_dicari_3007, "in", data_3007, "=", hasil_3007)

#operator not in
hasil_3007 = nilai_dicari_3007 not in data_3007
print("\nOperator keanggotaan NOT IN")
print("Apakah", nilai_dicari_3007, "not in", data_3007, "=", hasil_3007)

print("\n=====================================")
print("2. OPERATOR IDENTITAS")
print("=====================================")

# objek1 menggunakan list dari input pengguna
objek1_3007 =data_3007

# objek2 merujuk pada objek yang sama dengan objek1
objek2_3007 = objek1_3007

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_3007 = data_3007.copy()

print("objek1 =", objek1_3007)
print("objek2 =", objek2_3007)
print("objek3 =", objek3_3007)

# Operator is
hasil_3007 = objek1_3007 is objek2_3007
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_3007)

# Operator is not
hasil_3007 = objek1_3007 is not objek3_3007
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_3007)

# membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 == objek3 =", objek1_3007 == objek3_3007)
print("objek1 == objek3 =", objek1_3007 is objek3_3007)
