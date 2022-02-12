import itertools

while True:
    a = list(map(int, input().split()))

    if a[0] == 0:
        break

    a.pop(0)
    x = list(itertools.combinations(a, 6))
    for i in x:
        for j in i:
            print(j, end=" ")
        print()
    print()

