n = int(input())

arr = list(map(int, input().split()))

answer = 0
now = 0
for i in range(n):
    if arr[i] == now:
        answer += 1
        now += 1
        if now == 3:
            now = 0

print(answer)