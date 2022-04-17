from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def solution(places):
    answer = [1, 1, 1, 1, 1]

    for l in range(5):
        for i in range(5):
            if answer[l] == 0:
                break
            for j in range(5):
                if answer[l] == 0:
                    break
                distance = 0
                if places[l][i][j] == "P":
                    visit = [[0 for _ in range(5)] for _ in range(5)]
                    visit[i][j] = 1
                    q = deque()
                    q.append([i, j, distance])
                    while q:
                        x, y, distance = q.popleft()
                        if distance>= 3:
                            break
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0>nx or 5<=nx or 0>ny or 5<= ny:
                                continue
                            if places[l][nx][ny] =='O' and visit[nx][ny] == 0:
                                q.append([nx, ny, distance+1])
                                visit[nx][ny] = 1
                            if places[l][nx][ny] == 'P' and visit[nx][ny] == 0 and distance<= 1:
                                answer[l] = 0
                        if answer[l] == 0:
                            break



    return answer
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))