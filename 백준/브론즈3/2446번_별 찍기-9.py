n=int(input())
for i in range(1, n+1):
    print((" ")*(i-1) + "*"*(2*n-(2*i-1)))
for j in range(n-2, -1, -1):
    print(" "*j + "*"*((n-j)*2-1))