def sss(a, b):
    while a < b:
        if x[a] != x[b]:
            return 2

        a += 1
        b -= 1
    return 1

t = int(input())
for _ in range(t):
    x = list(input())
    a = 0
    b = len(x)-1
    cnt = 0
    while a<b:
        if x[a] != x[b]:
            if x[a+1] == x[b]:
                if x[a] == x[b-1] and cnt == 0:
                    if sss(a, b-1) == 1:
                        cnt = 1
                        break
                else:
                    a = a+1
                    cnt += 1
            elif x[a] == x[b-1]:
                b = b-1
                cnt += 1
            else:
                cnt = 2
                break
        a += 1
        b -= 1
        if cnt == 2:
            break

    print(cnt)

