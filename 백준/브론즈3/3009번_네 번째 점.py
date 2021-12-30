a, b= map(int, input().split())
c, d= map(int, input().split())
e, f= map(int, input().split())
x=[a, c, e]
y=[b, d, f]
xx=[]
yy=[]
x.sort()
y.sort()
xx.append(x[0])
if xx[0] == x[1]:
    print(x[2], end=" ")
else:
    print(xx[0], end=" ")
yy.append(y[0])
if yy[0] == y[1]:
    print(y[2])
else:
    print(yy[0])