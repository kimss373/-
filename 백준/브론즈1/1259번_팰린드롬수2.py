while True:
    x = str(input())
    if x == '0':
        break
    start=0
    end=len(x)-1
    xo=1
    while end>start:
        if x[start]!=x[end]:
            print("no")
            xo=0
            break
        end-=1
        start+=1
    if xo == 1:
        print("yes")