n = int(input("Please enter a number: "))
while n < 3 or n > 9:
    n = int(input("Please enter a number between 3 and 9: "))

rows = (2 * n) - 1

for i in range(1, rows + 1):
    diff = n - i
    if diff < 0:
        diff = -diff
    level = n - diff
    for j in range(1, level + 1):
        print(j, end="")

    print()
