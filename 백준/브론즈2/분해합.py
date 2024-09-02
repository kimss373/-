n = int(input())
answer = 0
for i in range(1, n+1):
    tmp = i
    result = tmp
    while tmp > 0:
        result += tmp%10
        tmp //= 10
    if result == n:
        answer = i
        break

print(answer)
