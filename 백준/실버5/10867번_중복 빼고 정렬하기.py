n = int(input())
x = list(map(int, input().split()))
x = list(set(x))
x.sort()
for i in x:
    print(i, end=" ")