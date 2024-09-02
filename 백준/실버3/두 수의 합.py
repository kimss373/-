n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()
idx1 = 0
idx2 = n-1
answer = 0
while idx1<idx2:
    tmp = arr[idx1] + arr[idx2]
    if tmp == x:
        answer += 1
        idx2 -= 1
        idx1 += 1
    elif tmp < x:
        idx1 += 1
    else:
        idx2 -= 1

print(answer)