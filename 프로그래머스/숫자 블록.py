def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        ox=1
        for j in range(2, int(i**(1/2))+1):
            if i%j == 0:
                if i//j >10000000:
                    continue
                else:
                    answer.append(i//j)
                    ox=0
                    break
        if ox==1:
            answer.append(1)
    if begin == 1:
        answer[0] = 0
    return answer