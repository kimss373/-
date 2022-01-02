m = int(input())
a=1000-m
n=[500, 100, 50, 10, 5, 1]
count=0
for i in n:
    while a>=i:
        a=a-i
        count += 1
print(count)