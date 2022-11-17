from collections import deque
def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    answer = 0
    for i in range(3*len(queue1)):
        if sum1 > sum2:
            x = queue1.popleft()
            sum1 -= x
            sum2 += x
            queue2.append(x)
            answer += 1

        elif sum2>sum1:
            x = queue2.popleft()
            sum2 -= x
            sum1 += x
            queue1.append(x)
            answer += 1

        else:
            return answer
    return -1


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))