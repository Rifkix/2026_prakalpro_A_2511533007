umur_3007= int(input("Input umur anda: "))
sim_3007 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0]

if umur_3007 >= 17 and sim_3007 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")

if umur_3007 >= 17 and sim_3007 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")

if umur_3007 < 17 and sim_3007 == 'y':
    print("Anda Belum Cukup umur punya SIM")

if umur_3007 < 17 and sim_3007 != 'y':
    print("Anda belum cukup umur bawa motor")