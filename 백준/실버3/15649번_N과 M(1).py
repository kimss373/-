import itertools
from itertools import permutations
a, b = map(int, input().split())
x = []
for i in range(1, a+1):
    x. append(str(i))

permutations_list = itertools.permutations(x, b)
for i in permutations_list:
    for j in range(len(i)):
        print(i[j], end=" ")
    print()