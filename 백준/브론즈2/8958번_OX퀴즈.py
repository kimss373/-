t=int(input())
y=[]
for i in range(t):
    x=list(map(str, input()))
    for j in range(len(x)):
        if x[j]=="X":
            y.append(0)
        elif x[j]=="O":
            if j==0:
                y.append(1)
            elif y[j-1] != 0:
                y.append(y[j-1]+1)
            else:
                y.append(1)
    print(sum(y))
    y.clear()