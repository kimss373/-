n = int(input())

cnt = 0
for i in range(1, n+1):
    tmp = str(i)
    sum = 0
    for j in range(len(tmp)):
        sum += int(tmp[j])

    if i % sum == 0:
        cnt += 1

print(cnt)