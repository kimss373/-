n = int(input())
m = int(input())

arr = list(map(int, input().split()))
arr.sort()

start = 0
end = n-1

answer = 0
while start < end:
    tmp = arr[start] + arr[end]
    if tmp == m:
        answer += 1
        start += 1
    elif tmp < m:
        start += 1
    else:
        end -= 1
print(answer)