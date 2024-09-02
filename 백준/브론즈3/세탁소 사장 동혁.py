n = int(input())

for i in range(n):
    tmp = int(input())
    print(tmp // 25, end=" ")
    tmp %= 25
    print(tmp // 10, end=" ")
    tmp %= 10
    print(tmp // 5, end=" ")
    tmp %= 5
    print(tmp)