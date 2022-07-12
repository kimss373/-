def solution(n):
    if int(n ** (1 / 2)) ** 2 == n:
        return (1 + n ** (1 / 2)) ** 2
    else:
        return -1
