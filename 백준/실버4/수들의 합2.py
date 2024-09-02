n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
sum = arr[0]
answer = 0
while start < n:
    if sum == m:
        answer += 1
        if end == n-1:
            break
        end += 1
        sum += arr[end]
    elif sum < m:
        if end == n-1:
            break
        end += 1
        sum += arr[end]
    else:
        sum -= arr[start]
        start += 1
print(answer)