n, k = map(int, input().split())
def factorial(n):
    a = 1
    for i in range(2, n+1):
        a *= i
    return a
print(int(factorial(n)/(factorial(k)*factorial(n-k))))