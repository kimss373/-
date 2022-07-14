from collections import deque
def solution(n, wires):
    answer = 100
    for i in range(len(wires)):
        a, b = wires[i]
        graph = [[] for i in range(n+1)]
        visit = [0 for i in range(n+1)]
        visit[a] = 1
        visit[b]= 1
        for j in range(len(wires)):
            if i == j:
                continue
            x, y = wires[j]
            graph[x].append(y)
            graph[y].append(x)

        alist = [a]
        blist = [b]
        q = deque()
        q.append(a)
        while q:
            z = q.popleft()
            for l in graph[z]:
                if visit[l] == 0:
                    q.append(l)
                    visit[l] = 1
                    alist.append(l)

        q.append(b)
        while q:
            z = q.popleft()
            for o in graph[z]:
                if visit[o] == 0:
                    q.append(o)
                    visit[o] = 1
                    blist.append(o)
        if abs(len(alist)-len(blist))<answer:
            answer = abs(len(alist)-len(blist))


    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))