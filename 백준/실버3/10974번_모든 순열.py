import itertools
n = int(input())
b = [i for i in range(1, n+1)]


a = list(itertools.permutations(b))
for j in a:
    for k in range(n):
        print(j[k], end=" ")
    print()