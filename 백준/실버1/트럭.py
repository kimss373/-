from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

leg = deque()

for i in range(w):
    leg.append(0)

sum = 0
count = 0
for i in range(n):
    while True:
        count += 1
        sum -= leg.popleft()
        if sum + trucks[i] <= L:
            leg.append(trucks[i])
            sum += trucks[i]
            break
        else:
            leg.append(0)
print(count + w)
