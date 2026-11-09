PASS_SCORE = 65
n = int(input("Number of student: "))

if n < 1:
    print("Invalid student count")
else:
    total = 0
    passed = 0
    lowest = 100

    for i in range(1, n+1):
        print("Student", i)
        score = int(input("Enter score:"))

        while score < 0 or score > 100:
            print("Invalid score")
            score = int(input("Enter score:"))

        total += score
        if score >= PASS_SCORE:
            passed += 1
        if score < lowest:
            lowest = score

    average = total / n
    print("Total score: " + str(total) + ", average score: " + str(round(average, 2)))
    print("Passed: " + str(passed))
    print("Lowest score: " + str(lowest))
