n=int(input())
for i in range(n):
    print("*"*(i+1), " "*(2*(n-i-1)), "*"*(i+1), sep="")
for j in range(n-1, 0, -1):
    print("*"*j, " "*2*(n-j-1), "*"*j)
