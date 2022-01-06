a=[tuple(input()) for _ in range(5)]
b=0
for l in range(5):
    if len(a[l])> b:
        b = len(a[l])
for i in range(b):
    for j in range(5):
        if len(a[j]) < i+1:
            pass
        else:
            print(a[j][i], end="")
