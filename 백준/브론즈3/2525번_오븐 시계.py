a, b = map(int, input().split())
c = int(input())

d, e = c//60, c%60

y = a+d
x = b+e
if x>=60:
    y += 1
    x -= 60
if y >= 24:
    y -= 24

print(y, x)