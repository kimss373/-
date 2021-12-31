t=int(input())
for i in range(t):
    a, b = map(int, input().split())
    if a>=10:
        a=a%10
    if b%4 == 0:
        b=4
    else:
        b=b%4
    if a==0:
        print("10")
    else:
        print(a**b%10)