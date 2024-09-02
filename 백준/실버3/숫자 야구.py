arr = []

visit = [0 for i in range(1, 10)]

def makeBaseBall(depth, visit, word):
    global arr
    if depth == 3:
        arr.append(word)
        return

    for i in range(9):
        if visit[i] == 0:
            visit[i] = 1
            makeBaseBall(depth+1, visit, word+str(i+1))
            visit[i] = 0


def baseReader(num, s, b, comparison):
    sCnt = 0
    bCnt = 0

    for i in range(len(num)):
        for j in range(len(comparison)):
            if num[i] == comparison[j]:
                if i == j:
                    sCnt += 1
                else:
                    bCnt += 1

    if int(s) == sCnt and int(b) == bCnt:
        return 'live'
    return 'del'

makeBaseBall(0, visit, '')

n = int(input())
for _ in range(n):
    num, s, b = map(str, input().split())
    for i in range(len(arr)):
        if arr[i] == '':
            continue
        result = baseReader(num, s, b, arr[i])
        if result == 'del':
            arr[i] = ''

print(len(arr)-arr.count(''))