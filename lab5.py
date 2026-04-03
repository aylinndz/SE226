def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

t = lambda l, i: (l ** i) / factorial(i)
def exp_x(x, n):
    if n == 0:
        return 1
    total=0

    for i in range(n):
        total += ((-1) ** i) * t(x, i)

    return total

num =0
def solution(n,k):
    '''This function prints out the absolute value of the entered number'''
    global num
    if n >= 0:
        num += (k ** n)
        solution(n - 1, k)

print("Output 2:", exp_x(5, 3))

solution(5, 3)
print("Output 3:", num)
