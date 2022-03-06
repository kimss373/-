import itertools

n, m =map(int, input().split())

a = list(map(int, input().split()))

combi = list(itertools.permutations(a, m))

for i in sorted(set(combi)):
    for j in i:
        print(j, end=" ")
    print()