n, kim, lim = map(int, input().split())
cnt = 0
if kim==1 and lim==2:
    print(1)
elif lim==1 and kim==2:
    print(1)
else:
    while True:
        if kim%2==0:
            kim = kim//2
        else:
            kim = kim//2 +1

        if lim%2 == 0:
            lim = lim//2
        else:
            lim = lim//2 +1

        cnt += 1

        if kim == lim:
            print(cnt)
            break