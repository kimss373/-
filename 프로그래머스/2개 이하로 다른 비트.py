def solution(numbers):
    answer = []
    for i in numbers:
        x = list('0' + bin(i)[2:])
        for j in range(len(x) - 1, -1, -1):
            if x[j] == '0':
                x[j] = '1'
                idx = j
                break
        if i % 2 == 1:
            x[idx + 1] = '0'
        answer.append(int(''.join(x), 2))
    return answer

print(solution([2, 7]))