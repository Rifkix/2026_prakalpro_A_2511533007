# Name: Rifki Maulana
# NIM: 2511533007
# Question 1

text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

text = "Rifki Maulana"
count = 0
for char in text.lower():
    if char in "aiueo":
        count += 1
print("Vowels:", count)
