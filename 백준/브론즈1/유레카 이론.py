import sys
input = sys.stdin.readline
t = int(input())

arr = []
num = 1
step = 1
while num <= 1000:
    arr.append(num)
    step += 1
    num += step

Aset = set()
tmp = 0
for i in range(len(arr)):
    tmp += arr[i]
    for j in range(len(arr)):
        tmp += arr[j]
        for k in range(len(arr)):
            tmp += arr[k]
            Aset.add(tmp)
            tmp -= arr[k]
        tmp -= arr[j]
    tmp -= arr[i]
for l in range(t):
    answer = int(input())
    if answer in Aset:
        print(1)
    else:
        print(0)
