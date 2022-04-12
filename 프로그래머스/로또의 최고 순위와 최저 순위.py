def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zerocnt = 0
    for i in lottos:
        if i == 0:
            zerocnt += 1
        elif i in win_nums:
            cnt+=1

    if cnt+zerocnt>=2:
        answer.append(7-(cnt+zerocnt))
    else:
        answer.append(6)
    if cnt>=2:
        answer.append(7-cnt)
    else:
        answer.append(6)
    return answer