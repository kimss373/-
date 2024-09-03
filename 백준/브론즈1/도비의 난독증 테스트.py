import sys
input = sys.stdin.readline

while True:
    arr = []
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        arr.append(input().rstrip())
    arr.sort(key= lambda x : x.upper())
    print(arr[0])


R1, S = map(int, input().split())