n = int(input())
a=0
b=1
for i in range(0, n+1):
    if i == 0:
        pass
    elif i == 1:
        pass
    elif i % 2 == 0:
        a=a+b
    else:
        b=a+b

if n%2==0:
    print(a)
else:
    print(b)
