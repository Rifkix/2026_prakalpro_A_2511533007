LAST_DIGIT = 7  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below
for day in range (1, 8):
    expense_input = int(input(f"Day {day}: ")) 
    expenses.append(expense_input)

total = 0
highest = expenses[0]
day_above_limit = 0
highest_day = 1

for i in range (len(expenses)):
    current = expenses[i]
    total += current
    if current > highest:
        highest = current
        highest_day = i + 1
    if current > daily_limit:
        day_above_limit += 1
        
average = total/len(expenses)

print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest})")
print(f"Days above limit: {day_above_limit}")
