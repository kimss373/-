a=list(input())
for i in range(len(a)//10+1):
    if len(a)>=10:
        for j in range(10):
            print(a[j], end="")
    else:
        for e in range(len(a)):
            print(a[e], end="")
    print()
    if len(a) >=10:
        for k in range(10):
            a.pop(0)
    else:
        for l in range(len(a)):
            a.pop(0)