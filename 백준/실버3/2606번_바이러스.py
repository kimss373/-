n = int(input())
m = int(input())
link_1 = [0] * (n + 1)
connect = []
que = [1]
for i in range(m):
    a, b = map(int, input().split())
    connect.append((a, b))

while que:
    a = que.pop(0)
    link_1[a] = 1
    for j in range(len(connect)):
        if connect[j][0] == a:
            que.append(connect[j][1])
            que.append(connect[j][0])
            connect.pop(j)
            break

        elif connect[j][1] == a:
            que.append(connect[j][0])
            que.append(connect[j][1])
            connect.pop(j)
            break

print(link_1.count(1) - 1)