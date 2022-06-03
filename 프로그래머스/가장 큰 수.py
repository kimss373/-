# def solution(numbers):
#     answer = ''
#     for i in range(len(numbers)):
#         numbers[i] = [str(numbers[i]), str(numbers[i]) * 3]
#
#     numbers.sort(key=lambda x: x[1])
#     for i in range(len(numbers) - 1, -1, -1):
#         answer += numbers[i][0]
#     return answer

def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])

    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer