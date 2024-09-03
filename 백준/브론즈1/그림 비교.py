n = int(input())

arr = []

for i in range(n):
    tmp = []
    for _ in range(5):
        tmp.append(input())
    arr.append(tmp)

maximum = 36
pair = ''
for i in range(n-1):
    for j in range(i+1, n):
        cnt = 0
        for k in range(5):
            for l in range(7):
                if arr[i][k][l] != arr[j][k][l]:
                    cnt += 1
        if cnt < maximum:
            maximum = cnt
            pair = str(i+1) + ' ' + str(j+1)

print(pair)