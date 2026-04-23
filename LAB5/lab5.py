def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)

t = lambda l, i: (l ** (2*i)) / factorial(2*i)
def exp_x(x, n):
    total=0

    for i in range(n):
        total += ((-1) ** i) * t(x, i)

    return total

num =0
def solution(n,k):
    '''This function takes parameter n and k then assigns
    the value to global variable y. It uses recursive logic
    to sum k^n terms and returns nothing.'''
    global num
    if n >= 0:
        num += (k ** n)
        solution(n - 1, k)

print("Output 2:", exp_x(5, 3))

solution(5, 3)
print("Output 3:", num)
