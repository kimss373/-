def solution(plans):
    answer = []
    stack = []

    for i in range(len(plans)):
        tmp = plans[i][1].split(":")
        plans[i][1] = int(tmp[0]) * 60 + int(tmp[1])
        plans[i][2] = int(plans[i][2])

    plans.sort(key=lambda x: x[1])

    now = plans[0][1]
    stack.append(plans.pop(0))

    while plans:

        if stack:
            if now + stack[-1][2] > plans[0][1]:
                stack[-1][2] -= plans[0][1] - now
                now = plans[0][1]
                stack.append(plans.pop(0))
            elif now + stack[-1][2] == plans[0][1]:
                answer.append(stack[-1][0])
                now = now + stack[-1][2]
                stack.pop()
                stack.append(plans.pop(0))
            else:
                answer.append(stack[-1][0])
                now = now + stack[-1][2]
                stack.pop()
        else:
            now = plans[0][1]
            stack.append(plans.pop(0))

    for i in range(len(stack)-1, -1, -1):
        answer.append(stack[i][0])


    return answer

print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "13:00", "30"], ["computer", "12:30", "100"]]))