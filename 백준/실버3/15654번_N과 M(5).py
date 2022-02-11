import itertools
n, m = map(int, input().split())

a = list(map(int, input().split()))
a.sort()
b=list(itertools.permutations(a, m))
for i in b:
    for j in i:
        print(j, end=" ")
    print()