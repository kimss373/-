n = int(input())
cnt = 0
for i in range(n):
    tmpList = []
    tmp = input()
    for j in tmp:
        if tmpList:
            if tmpList[-1] == j:
                tmpList.pop()
            else:
                tmpList.append(j)
        else:
            tmpList.append(j)
    if not tmpList:
        cnt += 1

print(cnt)
