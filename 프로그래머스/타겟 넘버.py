from itertools import product
plusminus = ['+', '-']

def solution(numbers, target):
    a = list(product(plusminus, repeat = len(numbers)))
    answer = 0
    for i in a:
        num = 0
        for j in range(len(numbers)):
            if i[j] == '+':
                num += numbers[j]
            elif i[j] == '-':
                num -= numbers[j]
        if num == target:
            answer += 1
    return answer

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))