def solution(s):
    x = len(s)
    answer = ''
    if x%2 == 0:
        answer = s[x//2 - 1 : x//2 + 1]
    else:
        answer = s[(x-1)//2]
    return answer