import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    tmp = list(map(int, input().split()))
    cnt = tmp.pop(0)
    dict = {}
    answer = "SYJKGW"
    for i in tmp:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in dict.keys():
        if dict[i] > cnt/2:
            answer = i
            break
    print(answer)