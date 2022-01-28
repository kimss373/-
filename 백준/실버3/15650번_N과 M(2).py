import itertools
a, b = map(int, input().split())
x = []
for i in range(1, a+1):
    x. append(str(i))

combinations_list = itertools.combinations(x, b)
for i in combinations_list:
    for j in range(len(i)):
        print(i[j], end=" ")
    print()