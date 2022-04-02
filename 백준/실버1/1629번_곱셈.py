def multiple(a, b):
    if b==1:
        return a%c

    temp = multiple(a, b//2)

    if b%2 == 0:
        return (temp*temp)%c
    else:
        return (temp*temp*a)%c


a, b, c = map(int, input().split())
print(multiple(a, b))

