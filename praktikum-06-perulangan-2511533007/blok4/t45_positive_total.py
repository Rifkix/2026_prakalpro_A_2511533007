bilInput = int(input("Enter a number: "))
positifNumber = 0

while bilInput >= 0:
    if bilInput == 0:
        bilInput = int(input("Enter a number: "))
        continue

    positifNumber += bilInput
    print("Positif number: ", positifNumber)
    bilInput = int(input("Enter a number: "))

print("Total: ", positifNumber)
print("program ended")
    