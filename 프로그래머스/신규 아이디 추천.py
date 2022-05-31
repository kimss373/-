def solution(new_id):
    permit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '_', '.']
    answer = ''

    new_id = new_id.lower()

    for i in new_id:
        if i in permit:
            answer += i

    tmp = answer[0]
    for i in range(1, len(answer)):
        if answer[i] == '.' and answer[i-1] == '.':
            continue
        tmp+=answer[i]

    if tmp and tmp[0] == '.':
        tmp = tmp[1:]

    if tmp and tmp[-1] == '.':
        tmp = tmp[:len(tmp)-1]

    if tmp == '':
        tmp = 'a'

    if len(tmp)>=16:
        tmp = tmp[:15]
        if tmp and tmp[-1] == '.':
            tmp = tmp[:len(tmp) - 1]

    if len(tmp)<=2:
        while len(tmp)<3:
            tmp += tmp[-1]

    return tmp

print(solution("123_.def"))