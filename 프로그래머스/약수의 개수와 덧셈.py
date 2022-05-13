def solution(left, right):
    answer = 0
    for i in range(left, right + 1):

        x = int(i ** (0.5))
        if x ** 2 == i:
            answer -= i
        else:
            answer += i

    return answer