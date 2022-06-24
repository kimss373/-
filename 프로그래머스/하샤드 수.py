def solution(x):
    x = str(x)
    value = 0
    for i in x:
        value += int(i)

    if int(x) % value == 0:
        return True
    else:
        return False