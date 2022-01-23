import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = sorted(list(set(a)))

dic = {b[i]:i for i in range(len(b))}

for j in a:
    print(dic[j], end=" ")