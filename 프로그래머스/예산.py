def solution(d, budget):
    answer = 0
    d.sort()
    while d:
        x = d.pop(0)
        if budget - x < 0:
            break
        budget -= x
        answer += 1

    return answer