import sys
input = sys.stdin.readline

a = {}
length = 0
while True:
    b = input().rstrip()
    if not b:
        break
    if b in a:
        a[b] += 1
    else:
        a[b] = 1
    length += 1
c = list(a.keys())
c.sort()

for i in c:
    print('%s %.4f' %(i, a[i]/length*100))
