x, y = map(str, input().split())
def Rev(x):
    x = str(x)
    a=[]
    for i in x:
        a.append(i)
    for j in range(len(a)//2):
        a[j], a[len(a)-j-1] = a[len(a)-j-1], a[j]
    b = 0
    for i in range(len(a)):
        b += int(a[i])*10**(len(a)-1-i)

    return b
c = Rev(x) + Rev(y)
print(Rev(c))
