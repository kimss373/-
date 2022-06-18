def solution(s, n):
    answer = []
    startlower = ord('a')
    endlower = ord('z')
    endupper = ord("Z")
    for i in s:
        if i == ' ':
            answer.append(' ')
            continue

        if startlower <= ord(i) <= endlower:
            if ord(i) + n > endlower:
                answer.append(chr(ord(i) + n - 26))
                continue
            answer.append(chr(ord(i) + n))
        else:
            if ord(i) + n > endupper:
                answer.append(chr(ord(i) + n - 26))
                continue
            answer.append(chr(ord(i) + n))
    return ''.join(answer)