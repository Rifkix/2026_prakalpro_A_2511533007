# Name: Rifki Maulana
# NIM: 2511533007
# Question 1

first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())

full_name = "Rifki Maulana"
nim = "2511533007"

# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().

clean = full_name.strip()
space = clean.find(" ")

if space == -1:
    first_name = clean
else:
    first_name = clean[:space]

username = first_name.lower() + nim[-3:]
print(username)