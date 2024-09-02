n = int(input())

now = 666

cnt = 0

while True:
    if "666" in str(now):
        cnt += 1
    if n == cnt:
        break
    now += 1

print(now)