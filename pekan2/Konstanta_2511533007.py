from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari = float(input("Masukkan nilai jari-jari: "))
luas = PI * jari * jari
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari, luas))
