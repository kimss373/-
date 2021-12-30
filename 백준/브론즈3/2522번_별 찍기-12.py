n=int(input())
for i in range(n):
    print(" "*(n-1-i) + "*"*(i+1))
for j in range(n-1, 0, -1):
    print(" "*(n-j) + "*"*j)