umur_3007 = int(input("Input umur anda: "))
sim_3007 = input("Apakah anda sudah punya SIM C: ")[0]

if umur_3007 >= 17 and sim_3007 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")

elif umur_3007 >= 17 and sim_3007 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")

elif umur_3007 < 17 and sim_3007 == 'y':
    print("Anda Belum Cukup umur punya SIM")

else:
    print("Anda belum cukup umur dan tidak boleh bawa motor")
print("Program selesai")
