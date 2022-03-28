import itertools

n = int(input())
Alist = list(map(int, input().split()))
arithmetic = list(map(int, input().split()))

operation = []
for i in range(4):
    if i==0:
        op = '+'
    elif i== 1:
        op = '-'
    elif i==2:
        op='*'
    else:
        op='/'
    for j in range(arithmetic[i]):
        operation.append(op)

combi = set(list(itertools.permutations(operation, n-1)))

max_result = -1000000000
min_result = 1000000000

for i in combi:
    cnt = Alist[0]
    for j in range(n-1):
        if i[j] == '+':
            cnt += Alist[j+1]
        elif i[j] == '-':
            cnt -= Alist[j+1]
        elif i[j] == '*':
            cnt *= Alist[j+1]
        else:
            if cnt < 0:
                cnt = -1*((-1*cnt)//Alist[j+1])
            else:
                cnt //= Alist[j+1]

    if cnt > max_result:
        max_result = cnt
    if cnt < min_result:
        min_result = cnt

print(max_result)
print(min_result)