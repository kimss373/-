day=input()
a, b, c, d, e=map(str, input().split())
car=[a, b, c, d, e]
x=0
for i in car:
    if day==i:
        x += 1
print(x)
print(car.count("3"))