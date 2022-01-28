import itertools
a, b = map(int, input().split())
x = []
for i in range(1, a+1):
    x.append(str(i))

combinations_with_replacement_list = itertools.combinations_with_replacement(x, b)
for i in combinations_with_replacement_list:
    for j in range(len(i)):
        print(i[j], end=" ")
    print()