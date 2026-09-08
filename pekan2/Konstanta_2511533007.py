from typing import Final
PI_3007: Final = 3.14
print("pi: %f" % (PI_3007))
jari_3007 = float(input("Masukkan nilai jari-jari: "))
luas_3007 = PI_3007 * jari_3007 * jari_3007
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3007, luas_3007))
