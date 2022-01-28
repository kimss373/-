import itertools
a, b = map(int, input().split())
x = []
for i in range(1, a+1):
    x.append(str(i))

product_list = itertools.product(x, repeat = b)
for i in product_list:
    for j in range(len(i)):
        print(i[j], end=" ")
    print()