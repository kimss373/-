def solution(people, limit):
    answer = 0
    people.sort()
    idx1 = 0
    idx2 = len(people)-1
    while idx1<idx2:
        if people[idx1]+people[idx2]>limit:
            answer+=1
            idx2 -=1

        elif people[idx1]+people[idx2]<=limit:
            answer += 1
            idx1 += 1
            idx2 -= 1

    if idx1==idx2:
        answer += 1

    return answer

print(solution([70, 50, 80, 50], 100))