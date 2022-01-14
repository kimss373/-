n=list(input())
n.sort(reverse=True)
value = 0
if '0' in n:
    for i in n:
        value += int(i)
    if value % 3 == 0:
        print(''.join(n))
    else:
        print(-1)
else:
    print(-1)