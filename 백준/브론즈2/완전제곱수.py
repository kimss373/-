m = int(input())
n = int(input())

answer = 0
min = -1
for i in range(1, 101):
    if m <= i ** 2 <= n:
        if min == -1:
            min = i ** 2
        answer += i ** 2

if min != -1:
    print(answer)
print(min)