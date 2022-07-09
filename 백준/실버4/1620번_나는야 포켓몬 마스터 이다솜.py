import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dicta = {}
dictb = {}
alpha = ['1','2', '3', '4', '5', '6' ,'7', '8', '9']
for i in range(1, n+1):
    a = input().rstrip()
    dicta[i] = a
    dictb[a] = i

for i in range(m):
    x = input().rstrip()
    if x[0] in alpha:
        print(dicta[int(x)])
    else:
        print(dictb[x])


