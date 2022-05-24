import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input())
        n = int(input())

        lego = []
        for _ in range(n):
            a = int(input())
            lego.append(a)
        lego.sort()
        length = x * 10000000

        answer = 'danger'

        idx1 = 0
        idx2 = n-1

        while idx1<idx2:
            if lego[idx1] + lego[idx2] == length:
                answer = 'yes ' + str(lego[idx1]) + ' ' + str(lego[idx2])
                break

            elif lego[idx1] + lego[idx2] < length:
                idx1 += 1

            else:
                idx2 -= 1

        print(answer)

    except:
        break
