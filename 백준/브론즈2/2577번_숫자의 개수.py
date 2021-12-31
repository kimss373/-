x=[]

for i in range(3):
    a=int(input())
    x.append(a)
y=str(x[0]*x[1]*x[2])
for j in range(10):
    print(y.count("{}".format(j)))