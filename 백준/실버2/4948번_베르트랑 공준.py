import sys
from math import sqrt
input = sys.stdin.readline


def prime(n):
    if n==1:
        return False
    else:
        for i in range(2, int(sqrt(n))+1):
            if n% i==0:
                return False
    return True

primelist = []
for i in range(2, 246912):
    if prime(i):
        primelist.append(i)

n = int(input())
while n != 0:
    answer = 0

    for i in primelist:
        if n<i <= n*2:
            answer += 1
    print(answer)
    n = int(input())