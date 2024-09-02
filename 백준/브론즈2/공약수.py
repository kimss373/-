n = int(input())

arr = list(map(int, input().split()))
arr.sort()

result = set([])

for i in range(1, int(arr[0]**0.5) + 2):
    if arr[0]%i == 0:
        isSmalla = True
        isSmallb = True
        for j in range(n):
            if arr[j] % i != 0:
                isSmalla = False
            if arr[j] % (arr[0]//i) != 0:
                isSmallb = False
        if isSmalla:
            result.add(i)
        if isSmallb:
            result.add(arr[0]//i)

result_list = sorted(list(result))
for i in result_list:
    print(i)