x={}
a=0
for i in range(1, 10):
    x[i]=int(input())

for j in range(1, 10):
    if x[j]>a:
        a=x[j]
print(a)
for key in x.keys():
    if a==x[key]:
        print(key)