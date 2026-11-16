# Name: Rifki Maulana
# NIM: 2511533007
# Question 1

sentence = input("Masukkan kalimat: ")
cleaned = ""
for char in sentence.lower():
    if char != " ":
        cleaned += char

reversed_str = cleaned[::-1]

if cleaned == reversed_str:
    print("Palindrome")
else:
    print("Not a palindrome")