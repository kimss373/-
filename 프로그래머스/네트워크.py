from collections import deque

q = deque()
result = []
def solution(n, computers):
    answer = 0
    for i in range(n):
        if i in result:
            continue
        for j in range(n):
            if computers[i][j] == 1 and j not in result:
                q.append(j)
                result.append(j)
                answer+=1
                while q:
                    x = q.popleft()
                    for k in range(n):
                        if computers[x][k] ==1 and k not in result:
                            result.append(k)
                            q.append(k)
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
result = [0]
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))