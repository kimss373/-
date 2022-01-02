a=list(map(int, input().split()))
b=[]
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        b.append(1)
    else:
        b.append(0)
if sum(b) == 7:
    print("ascending")
elif sum(b) == 0:
    print("descending")
else:
    print("mixed")