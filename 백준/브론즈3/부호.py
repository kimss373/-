for _ in range(3) :
    n = int(input())
    tmp = 0
    for i in range(n):
        tmp += int(input())

    if tmp < 0:
        print('-')
    elif tmp == 0:
        print(0)
    else:
        print('+')