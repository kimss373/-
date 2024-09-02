t = int(input())
for i in range(t):
    n = int(input())
    tmp = list(map(int, input().split()))
    price = 0
    answer = 0
    for j in range(n-1, -1, -1):
        if tmp[j] <= price:
            answer += price-tmp[j]
        else:
            price = tmp[j]
    print(answer)