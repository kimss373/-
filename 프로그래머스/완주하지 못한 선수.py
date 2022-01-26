def solution(participant, completion):

    part = {}
    for i in participant:
        part[i] = 0
    for k in participant:
        part[k] += 1
    for l in completion:
        part[l] -= 1

    for key in part:
        if part[key] == 1:
            answer = key
            break
    return answer

x = solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
print(x)