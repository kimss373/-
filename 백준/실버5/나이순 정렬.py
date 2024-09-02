import sys
input = sys.stdin.readline


n = int(input())

arr = []
for i in range(n):
    tmp = list(map(str, input().split()))
    tmp[0] = int(tmp[0])
    tmp.append(i)
    arr.append(tmp)

arr.sort(key=lambda x: (x[0], x[2]))

for i in range(n):
    print(arr[i][0], arr[i][1])