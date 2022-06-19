def solution(s):
    s = list(s)
    tmp = 0
    for i in range(len(s)):
        if s[i] == ' ':
            tmp = 0
            continue
        if tmp % 2 == 0:
            s[i] = s[i].upper()
            tmp += 1
        else:
            s[i] = s[i].lower()
            tmp += 1

    return ''.join(s)