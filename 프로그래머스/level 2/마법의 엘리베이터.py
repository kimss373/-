def solution(storey):
    answer = 0

    while storey:
        num = storey % 10
        if num >= 6:
            storey += 10 - num
            answer += 10 - num
        elif num == 5:
            if (storey // 10) % 10 >= 5:
                storey += 10 - num
                answer += 10 - num
            else:
                answer += num
        else:
            answer += num
        storey //= 10

    return answer