# Name: Rifki Maulana
# NIM: 2511533007
# Question 1

full_name = "rifki maulana"
nim = "2511533007"

name = full_name.strip().lower()

space = name.find(" ")
if space == -1:
    first_name = name
else:
    first_name = name[:space]
username = first_name + nim[-3:]

intake = "20" + nim[:2]

line = "=" * 30
print(line)
print("STUDENT CARD".center(30))
print(line)
print(f"{'Name':<10} : {name.title()}")
print(f"{'NIM':<10} : {nim}")
print(f"{'Username':<10} : {username}")
print(f"{'Intake':<10} : {intake}")
print(line)