import itertools

n, m = map(int, input().split())

a = list(map(int, input().split()))

b = list(set(a))
b.sort()
c = list(itertools.combinations_with_replacement(b, m))

for i in c:
    for j in i:
        print(j, end=" ")
    print()