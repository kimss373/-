x=int(input())
b = 1
a= 1
while a < x:
    b += 1
    a = a + b
if b%2 == 0:
    c = b
    d = 1
    c += x-a
    d -= x-a
else:
    d = b
    c = 1
    c -= x-a
    d += x-a
print(c, "/", d, sep="")