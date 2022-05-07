def solution(n, words):
    answer = [0, 0]
    person = 2
    bun = 1
    record = [words[0]]
    x = 1
    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][-1]:
            x = 0
            break
        elif words[i] in record:
            x = 0
            break
        record.append(words[i])
        if person == n:
            person = 1
            bun += 1
        else:
            person += 1

    if x == 0:
        answer = [person, bun]

    return answer