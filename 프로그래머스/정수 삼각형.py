def solution(triangle):
    arr = []
    for i in range(len(triangle)):
        x = [0 for i in range(i + 1)]
        arr.append(x)

    arr[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0:
                arr[i][j] = arr[i - 1][0] + triangle[i][j]
            elif j == i:
                arr[i][j] = triangle[i][j] + arr[i - 1][i - 1]
            else:
                arr[i][j] = triangle[i][j] + max(arr[i - 1][j], arr[i - 1][j - 1])
    answer = max(arr[-1])
    return answer