menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below
for day in range(1, number_of_days + 1):
    row = []
    for menu in menus:
        jml = int(input(f"Day {day}, {menu}: "))
        row.append(jml)
    sales.append(row)

print("Total per day:")

for i in range(number_of_days):
    day_total = 0
    for j in range(len(menus)):
        day_total += sales[i][j]
    print(f"Day {i + 1}: {day_total}")

menu_totals = []

for j in range(len(menus)):
    menu_total = 0
    for i in range(number_of_days):
        menu_total += sales[i][j]
    menu_totals.append((menus[j], menu_total))

print(f"Total per menu: {menu_totals}")

best_name, best_total = menu_totals[0]
for name, total in menu_totals:
    if total > best_total:
        best_total = total
        best_name = name

print(f"Best seller: {best_name} ({best_total})")