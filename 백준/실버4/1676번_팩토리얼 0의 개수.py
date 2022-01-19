n=int(input())
factorial = 1
for i in range(1, n+1):
    factorial *= i

zero = 0
while True:
    if factorial % 10 == 0:
        zero += 1
    else:
        break

    factorial = factorial // 10
print(zero)