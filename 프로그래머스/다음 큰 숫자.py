def solution(n):
    binaryNum = format(n, 'b')
    a = list(binaryNum)
    print(a)
    xo = 0
    for i in range(len(a)):
        if xo == 1:
            break

        if a[i] == '0':
            for j in range(i+1, len(a)):
                if a[j] == '1':
                    a.insert(j-1, a.pop(j))
                    xo = 1
                    break
            if xo==0:
                for k in range(len(a)-i):
                    a.insert(1, a.pop())
                a.insert(1, '0')

    if xo==0:
        a.insert(1, '0')
    print(a)
    x = ''
    for i in a:
        x += i
    z = int(x, 2)

    return z

print(solution(78))
