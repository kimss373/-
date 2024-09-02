n, k = map(int, input().split())

arr = list(map(int, input().split()))

tmp = sum(arr[0:k])
answer = tmp

for i in range(1, n-k+1):
    tmp = tmp - arr[i-1] + arr[i+k-1]
    answer = max(answer, tmp)

print(answer)