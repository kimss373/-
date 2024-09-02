n = int(input())
arr = list(map(int, input().split()))

arr.sort()

answer = 0
sum = 0
for i in arr:
    answer += sum + i
    sum += i

print(answer)