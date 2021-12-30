x, y, w, h=map(int, input().split())
if x>=w/2:
    a=w-x
else:
    a=x
if y>=h/2:
    b=h-y
else:
    b=y
if a<=b:
    print(a)
else:
    print(b)