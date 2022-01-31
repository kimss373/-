def solution(clothes):
    answer = 1
    diction = {}
    for i in clothes:
        diction[i[1]] = 0
    for j in clothes:
        diction[j[1]] += 1

    for k in diction:
        answer *= (diction[k]+1)
    answer = answer -1
    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))