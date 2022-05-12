def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = []
        for k in range(len(arr2[0])):
            x = 0
            for j in range(len(arr1[0])):
                x += arr1[i][j] * arr2[j][k]
            tmp.append(x)
        answer.append(tmp)

    return answer