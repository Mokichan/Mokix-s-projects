n = int(input())

def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1)*n

factorial(n)
print(factorial(n))