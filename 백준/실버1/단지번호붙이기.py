from collections import deque
n = int(input())
arr = [list(input()) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()

cnt = 1
answer = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1':
            cnt1 = 1
            cnt += 1
            arr[i][j] = cnt
            q.append([i, j])
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == '1':
                        cnt1 += 1
                        arr[nx][ny] = cnt
                        q.append([nx,ny])
            answer.append(cnt1)
print(cnt-1)
answer.sort()
for i in answer:
    print(i)
print(arr)
