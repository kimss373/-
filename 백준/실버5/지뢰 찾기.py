dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

n = int(input())

arr = []

for i in range(n):
    arr.append(input())

for i in range(n):
    tmp = ''

    for j in range(n):
        if arr[i][j] != '.':
            tmp += '*'
            continue
        tmpNum = 0
        for k in range(8):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != '.':
                tmpNum += int(arr[nx][ny])
        if tmpNum >= 10:
            tmpNum = 'M'
        tmp += str(tmpNum)
    print(tmp)