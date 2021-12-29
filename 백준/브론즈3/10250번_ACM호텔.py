t=int(input())
for i in range(t):
    h, w, n=map(int,input().split())
    if n%h==0 and n//h<10:
        print(h, "0", n//h, sep="")
    elif n%h==0 and n//h>=10:
        print(h, n // h, sep="")
    elif n//h+1<10:
        print(n%h,"0", n//h+1, sep="")
    else:
        print(n % h, n // h + 1, sep="")
