from itertools import combinations

def solution(numbers):
    answer = []
    x = list(combinations(numbers, 2))
    for i in x:
        a, b = i
        answer.append(a+b)

    answer = sorted(list(set(answer)))
    return answer

print(solution([2,1,3,4,1]))