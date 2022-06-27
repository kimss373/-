def solution(n):
    answer = 0
    x = list(str(n))
    x.sort(reverse = True)
    answer = int(''.join(x))
    return answer