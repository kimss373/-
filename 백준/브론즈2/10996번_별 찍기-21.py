n=int(input())

for j in range(1, n+1):
    if n%2 != 0:
        print("* "*(n//2) + "*")
    elif n%2 ==0:
        print("* "*(n//2))

    if n==1:
        pass
    elif n%2 !=0:
        print(" *"*(n//2))
    elif n%2 ==0 :
        print(" *"*(n//2))
