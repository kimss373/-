def solution(sequence, k):

    answer = []
    sum = 0
    head = -1
    tail = 0

    while True:
        if sum<k:
            head += 1
            if head >= len(sequence):
                break
            sum += sequence[head]
        else:
            sum -= sequence[tail]
            tail += 1

        if sum == k:
            answer.append([tail, head])

    answer.sort(key=lambda x: (x[1]-x[0], x[0]))

    return answer[0]

print(solution([1, 1, 1, 2, 3, 4, 5], 5))