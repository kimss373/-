import itertools
n, s = map(int, input().split())

num = list(map(int, input().split()))
num.insert(0, 0)
x = [i for i in range(1, n+1)]
cnt = 0
for i in range(1, n+1):
    a = list(itertools.combinations(x, i))

    for j in a:
        b=0
        for k in j:
            b += num[k]
        if b == s:
            cnt += 1
print(cnt)