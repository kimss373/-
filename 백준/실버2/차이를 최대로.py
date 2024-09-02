n = int(input())
arr = list(map(int, input().split()))

visit = [0 for _ in range(n)]
calArr = []

max = 0
cnt = 0
def maxDiff(depth):
    global arr
    global visit
    global calArr
    global max
    global n

    if depth == n:
        tmp = 0
        for i in range(n-1):
            tmp += abs(calArr[i]-calArr[i+1])
        if tmp > max:
            max = tmp

    for i in range(n):
        if visit[i] == 0:
            calArr.append(arr[i])
            visit[i] = 1
            maxDiff(depth+1)
            calArr.pop()
            visit[i] = 0

maxDiff(0)

print(max)