n=int(input())
a = n
if n != 1:
    for i in range(2, n+1):
        while a % i == 0:
            a = a//i
            print(i)
