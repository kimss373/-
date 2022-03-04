import math
a, b = map(int, input().split())

for i in range(math.gcd(a, b)):
    print(1, end="")
