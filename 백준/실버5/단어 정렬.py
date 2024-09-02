import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    arr.append(input().rstrip())

arr.sort(key=lambda x : (len(x), x))

recent = ''
for i in arr:
    if i == recent:
        continue
    print(i)
    recent = i

