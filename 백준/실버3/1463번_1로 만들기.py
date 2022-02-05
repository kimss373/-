x = int(input())

xn = [0]*(x+1)
# 0 0 1 1 2 0 0 0 0 0 0
for i in range(2, x+1):
    xn[i] = xn[i-1] + 1

    if i%3 == 0:
        xn[i] = min(xn[i], xn[i//3] +1)
    if i%2 == 0:
        xn[i] = min(xn[i], xn[i//2] +1)
print(xn[x])