import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    arr = []
    for j in range(n):
        arr.append(list(map(int, input().split())))
    arr.sort(key=lambda x:x[0])
    min = arr[0][1]
    cnt = 1
    for j in range(1, n):
        if arr[j][1] < min:
            cnt += 1
            min = arr[j][1]

    print(cnt)

