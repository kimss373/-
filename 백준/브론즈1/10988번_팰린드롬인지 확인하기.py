a = input()
b=[]
for i in range(len(a)//2):
    if a[i] == a[len(a)-i-1]:
        b.append(1)
    else:
        b.append(0)
if 0 in b:
    print(0)
else:
    print(1)