def solution(progresses, speeds):
    timee = []
    stack = []
    answer = []
    for i in range(len(progresses)):
        if (100-progresses[i]) % speeds[i] == 0:
            timee.append((100-progresses[i])//speeds[i])
        else:
            timee.append((100-progresses[i])//speeds[i]+1)
    for j in range(len(progresses)):
        count = 0
        while stack and timee[j]>stack[0]:
            stack.pop()
            count += 1
        if count != 0:
            answer.append(count)
        stack.append(timee[j])
    if stack:
        answer.append(len(stack))
    return answer
