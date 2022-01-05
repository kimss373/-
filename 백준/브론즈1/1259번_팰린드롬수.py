while True:
    a=str(input())
    if a == "0":
        break
    b = []
    for i in range(len(a)//2):
        if a[i] == a[len(a)-i-1]:
            b.append(0)
        else:
            b.append(1)
    if 1 in b:
        print("no")
    else:
        print("yes")