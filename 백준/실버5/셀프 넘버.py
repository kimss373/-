notSelfNumber = set()

for i in range(1, 10000):
    tmp = i
    while i > 0:
        tmp += i % 10
        i //= 10
    notSelfNumber.add(tmp)

for i in range(1, 10000):
    if i in notSelfNumber:
        continue
    print(i)