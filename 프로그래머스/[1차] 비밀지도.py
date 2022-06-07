def solution(n, arr1, arr2):
    answer = []
    list1 = []
    list2 = []
    for i in arr1:
        x = str(bin(i)[2:])
        while len(x) < n:
            x = '0' + x
        list1.append(list(x))

    for i in arr2:
        x = str(bin(i)[2:])
        while len(x) < n:
            x = '0' + x
        list2.append(list(x))

    for i in range(n):
        y = ''
        for j in range(n):
            list1[i][j] = int(list2[i][j]) + int(list1[i][j])
            if list1[i][j] == 0:
                y += ' '
            else:
                y += '#'
        answer.append(y)
    return answer

print(solution(5, [9, 20, 28, 18, 11], 	[30, 1, 21, 17, 28]))