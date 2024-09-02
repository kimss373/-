x, y = map(int, input().split())

people = []

for i in range(3):
    people.append(list(map(int, input().split())))

visit = [0 for _ in range(len(people))]

answer = 50000
def combi(depth, visit, leng, now):
    global answer
    if depth == 3:
        if leng < answer:
            answer = leng
        return

    for i in range(3):
        if visit[i] == 0:
            visit[i] = 1
            combi(depth+1, visit, leng + ((now[0]-people[i][0])**2 + (now[1] - people[i][1])**2)**0.5, people[i])
            visit[i] = 0

combi(0, visit, 0, [x, y])
print(int(answer))