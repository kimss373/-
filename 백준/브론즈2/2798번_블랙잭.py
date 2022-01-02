from itertools import combinations
n, m = map(int, input().split())
card = list(map(int, input().split()))
com = list(combinations(card, 3))
a=[]
for i in range(len(com)):
    if sum(com[i])>m:
        pass
    else:
        a.append(sum(com[i]))
a.sort()
print(a[-1])