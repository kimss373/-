x=[]
y=[]
for i in range(10):
    x.append(int(input()))
for j in range(10):
    if x[j]%42 in y:
        pass
    else:
        y.append(x[j]%42)
print(len(y))