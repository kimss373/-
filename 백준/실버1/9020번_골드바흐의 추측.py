import sys
input = sys.stdin.readline

def isPrime(x):
    y = x**0.5
    y = int(y)
    for i in range(2, y+1):
        if x%i==0:
            return False
    return True


t = int(input())
for _ in range(t):
    n = int(input())
    a = n//2
    b = n//2
    while isPrime(a)==False or isPrime(b)==False:
        a -= 1
        b += 1
    print(a, b)


