t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    tmpList = list(map(int, input().split()))
    cnt = 1

    while True:
        isImportant = True
        for i in range(1, len(tmpList)):
            if tmpList[i] > tmpList[0]:
                tmpList.append(tmpList.pop(0))
                isImportant = False
                m -= 1
                if m < 0:
                    m = len(tmpList)-1
                break

        if isImportant:
            if m == 0:
                print(cnt)
                break
            else:
                tmpList.pop(0)
                cnt += 1
                m -= 1

