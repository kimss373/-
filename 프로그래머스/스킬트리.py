def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        dict = {}
        k = 0
        for j in skill:
            dict[j] = k
            k -= 1

        x = 0
        for l in i:
            if l in dict:
                if dict[l] == 0:
                    for v in dict:
                        dict[v] += 1
                else:
                    x = 1
                    break

        if x == 0:
            answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))