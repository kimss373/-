n = int(input())  # n보다 작거나 같은 한수의 개수

count = 0  # 100상 1000이하의 수 중 한수의 개수

if n < 100:  # 100미만은 전부 한수
    print(n)
else:         # 100 이상의 수 중 한수의 개수 + 99
    for i in range(100, n+1):
        if int(str(i)[0])-int(str(i)[1]) == int(str(i)[1])-int(str(i)[2]):
            count += 1
    print(99 + count)