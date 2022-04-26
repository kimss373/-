from itertools import combinations


def solution(nums):
    answer = 0
    combi = list(combinations(nums, 3))

    for i in combi:
        tmp = 0
        x = 0
        for j in i:
            tmp += j
        tmp1 = int(tmp ** (0.5))
        for k in range(2, tmp1 + 1):
            if tmp % k == 0:
                x = 1
        if x == 0:
            answer += 1

    return answer

solution([1, 2, 3, 4])