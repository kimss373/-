n = int(input())

change = 1000 - n

arr = [500, 100, 50, 10, 5, 1]

cnt = 0
for i in arr:
    cnt += change // i
    change %= i

print(cnt)