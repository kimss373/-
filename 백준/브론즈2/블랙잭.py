n, m = map(int, input().split())
global arr
arr = list(map(int, input().split()))
global visit
visit = [0 for _ in range(n)]
global black
black = m
global answer
answer = 0
def blackJack(depth, sumVal, start):
    global answer
    if depth == 3:
        if sumVal <= black and sumVal > answer:
            answer = sumVal
        return
    for i in range(start, n):
        if visit[i] == 0:
            visit[i] = 1
            blackJack(depth + 1, sumVal + arr[i], i+1)
            visit[i] = 0

blackJack(0, 0, 0)
print(answer)

