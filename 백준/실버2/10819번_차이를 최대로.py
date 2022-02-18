import itertools
t = int(input())

a = list(map(int, input().split()))

max = 0
for i in list(itertools.permutations(a, t)):
    x = 0
    for j in range(t-1):
        x += abs(i[j]-i[j+1])

    if x > max:
        max = x

print(max)