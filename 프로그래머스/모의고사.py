def solution(answers):
    a = [1, 2, 3, 4, 5]*2000
    b = [2, 1, 2, 3, 2, 4, 2, 5]*1250
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000
    a_cnt = 0
    b_cnt = 0
    c_cnt = 0
    answer = []
    for i in range(len(answers)):
        if a[i] == answers[i]:
            a_cnt+=1
        if b[i] == answers[i]:
            b_cnt += 1
        if c[i] == answers[i]:
            c_cnt += 1
    if max(a_cnt, b_cnt, c_cnt) == a_cnt:
        answer.append(1)
    if max(a_cnt, b_cnt, c_cnt) == b_cnt:
        answer.append(2)
    if max(a_cnt, b_cnt, c_cnt) == c_cnt:
        answer.append(3)



    return answer