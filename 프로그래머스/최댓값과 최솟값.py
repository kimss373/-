def solution(s):
    answer = ''
    result = []
    tmp = ''
    for i in s:
        if i == ' ':
            if tmp[0] == '-':
                result.append(int(tmp[1:]) * -1)
            else:
                result.append(int(tmp))
            tmp = ''
        else:
            tmp += i
    if tmp[0] == '-':
        result.append(int(tmp[1:]) * -1)
    else:
        result.append(int(tmp))

    result.sort()
    answer = str(result[0]) + ' ' + str(result[-1])
    return answer