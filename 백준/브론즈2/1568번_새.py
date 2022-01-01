n=int(input())
i=1
count = 0
while True:
    n=n-i
    count += 1
    i += 1
    if n<i:
        i=1
    if n==0:
        break

print(count)