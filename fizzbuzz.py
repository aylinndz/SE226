n = int(input("enter number: "))
while n<10 or n>100:
    n = int(input("enter number between 10-100: "))
    fizz=0
    buzz=0
    fizzbuzz=0

for i in range(1,n+1):
    if i%7==0:
        print(i , "skip" )
        continue

    elif i %3==0 and i % 5 ==0:
        print("fizzbuzz")


    elif i %3==0:
        print("fizz")

    elif i % 5 ==0:
        print("buzz")

    else:
        print(i)

