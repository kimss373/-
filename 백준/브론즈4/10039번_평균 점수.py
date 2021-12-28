x=[]
for i in range(5):
    y=int(input())
    if y<40:
        x.append(40)
    else:
        x.append(y)

print(sum(x)//5)
