def solution(dirs):
    answer = 0
    now = [0, 0]
    visit = []
    for i in range(len(dirs)):

        a = now[0]
        b = now[1]
        if dirs[i] == 'U':
            if b + 1 > 5:
                continue
            if str(a) + str(b) + str(a) + str(b + 1) in visit or str(a) + str(b + 1) + str(a) + str(b) in visit:
                now = [a, b + 1]
                continue
            visit.append(str(a) + str(b) + str(a) + str(b + 1))
            visit.append(str(a) + str(b + 1) + str(a) + str(b))
            answer += 1
            now = [a, b + 1]
        elif dirs[i] == 'D':
            if b - 1 < -5:
                continue
            if str(a) + str(b) + str(a) + str(b - 1) in visit or str(a) + str(b - 1) + str(a) + str(b) in visit:
                now = [a, b - 1]
                continue
            visit.append(str(a) + str(b) + str(a) + str(b - 1))
            visit.append(str(a) + str(b - 1) + str(a) + str(b))
            answer += 1
            now = [a, b - 1]
        elif dirs[i] == 'R':
            if a + 1 > 5:
                continue
            if str(a) + str(b) + str(a + 1) + str(b) in visit or str(a + 1) + str(b) + str(a) + str(b) in visit:
                now = [a + 1, b]
                continue
            visit.append(str(a + 1) + str(b) + str(a) + str(b))
            visit.append(str(a) + str(b) + str(a + 1) + str(b))
            answer += 1
            now = [a + 1, b]
        else:
            if a - 1 < -5:
                continue
            if str(a) + str(b) + str(a - 1) + str(b) in visit or str(a - 1) + str(b) + str(a) + str(b) in visit:
                now = [a - 1, b]
                continue
            visit.append(str(a - 1) + str(b) + str(a) + str(b))
            visit.append(str(a) + str(b) + str(a - 1) + str(b))
            answer += 1
            now = [a - 1, b]

    return answer

print(solution("ULURRDLLU"))