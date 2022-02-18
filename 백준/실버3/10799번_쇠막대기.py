a = list(input())

cnt = 0

x = 0
for i in range(len(a)):
    if a[i] == '(':
        x += 1
    else:
        if a[i-1] == '(':
            x -= 1
            cnt += x
        else:
            x -= 1
            cnt += 1

print(cnt)