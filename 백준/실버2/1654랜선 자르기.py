import sys

input = sys.stdin.readline

k, n = map(int, input().split())

list1 = []
for i in range(k):
    list1.append(int(input()))

start = 1
end = max(list1)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(k):
        cnt += list1[i]//mid

    if cnt < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)