def solution(phone_number):
    x = list(phone_number)
    for i in range(len(phone_number) - 4):
        x[i] = '*'

    return ''.join(x)