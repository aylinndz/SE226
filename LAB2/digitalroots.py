num = int(input("Please enter a positive integer greater than 9: "))

while num <=9:
    num = int(input("Please enter a positive integer greater than 9: "))

total = 0
print(num ,end="")

while num > 9:
    sumOfDigits = 0
    temp = num

    while temp > 0:
        last_digit = temp % 10
        sumOfDigits = sumOfDigits + last_digit
        temp = temp // 10

    num = sumOfDigits
    total = total + 1

    print(" -", num ,end="")
print()
print("Final value:", num)
print("Total steps:", total)
