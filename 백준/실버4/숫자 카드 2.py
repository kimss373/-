import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

diction = {}

for i in arr1:
    if i in diction:
        diction[i] += 1
    else:
        diction[i] = 1

for i in arr2:
    if i in diction:
        print(diction[i], end=" ")
    else:
        print(0, end=" ")