import sys
input = sys.stdin.readline
print = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))
    tmpSet=set()
    for i in range(n):
        tmpSet.add(note1[i])
    for i in range(m):
        if note2[i] in tmpSet:
            print('1\n')
        else:
            print('0\n')
