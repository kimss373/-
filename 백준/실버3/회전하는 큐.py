n, m = map(int, input().split())

deque = [i for i in range(1, n+1)]
want = list(map(int, input().split()))

cnt = 0

for i in range(m):
    idx = deque.index(want[i])
    cnt += min(len(deque)-idx, idx)
    for _ in range(idx):
        deque.append(deque.pop(0))
    deque.pop(0)

print(cnt)