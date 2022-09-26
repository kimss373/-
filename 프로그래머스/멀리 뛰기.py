def solution(n):
    x = [1, 2]
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(n-2):
            x.append((x[-1] + x[-2])%1234567)

        return x[-1]%1234567


