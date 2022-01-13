x=int(input())
count = 0
while True:
    for i in range(6, -1, -1):
        if x-2**i >= 0:
            x = x-2**i
            count += 1

    if x == 0:
        break
print(count)