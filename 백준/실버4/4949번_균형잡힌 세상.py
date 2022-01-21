# https://www.acmicpc.net/problem/4949
while True:
    a = list(input())
    if a == ['.']:      # '.'만 입력되면 종료
        break
    length = len(a)
    for i in range(length-1, -1, -1):   # ()[]가 아니면 배열에서 제거
        if a[i] != '(' and a[i] != ')' and a[i] != '[' and a[i] != ']':
            a.pop(i)

    while True:     #  (다음에 바로 ) 또는 [다음 바로 ]면 제거
        x = 0
        for j in range(len(a)-1):
            if a[j] == '(' and a[j+1] == ')':
                a.pop(j)
                a.pop(j)
                x = 1
                break
            elif a[j] == '[' and a[j+1] == ']':
                a.pop(j)
                a.pop(j)
                x = 1
                break
        if x == 0:
            break

    if not a:
        print('yes')
    else:
        print('no')