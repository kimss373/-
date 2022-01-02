from itertools import combinations
tall = []
for i in range(9):
    tall.append(int(input()))
com_tall = list(combinations(tall, 7))
for j in range(len(com_tall)):
    if sum(com_tall[j]) == 100:
        a=list(com_tall[j])
        a.sort()
        for k in range(7):
            print(a[k])
        break