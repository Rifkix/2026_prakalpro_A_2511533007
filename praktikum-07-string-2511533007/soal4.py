# Name: Rifki Maulana
# NIM: 2511533007
# Question 1

phone = "082511533007"
masked = phone[:4] + "*" * (len(phone)-7) + phone[-3:]
print(masked)
