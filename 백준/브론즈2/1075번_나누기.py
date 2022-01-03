n=int(input())
f=int(input())
if (n-(n%f))%100<=n%100:
    if len(str(((n-(n%f))%100)%f)) == 1:
        print("0" + str(((n - (n % f)) % 100) % f))
    else:
        print(((n-(n%f))%100)%f)
elif (n-(n%f))%100>n%100:
    if len(str((n+f-(n%f))%100)) == 1:
        print("0" + str((n + f - (n % f)) % 100))
    else:
        print((n+f-(n%f))%100)
