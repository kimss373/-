n = int(input())

for i in range(n, 3, -1):
    tmp = str(i)
    if len(tmp) == tmp.count('4') + tmp.count('7'):
        print(i)
        break
