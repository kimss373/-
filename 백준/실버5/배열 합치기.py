n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.extend(arr2)
arr1.sort()
for i in range(n+m):
    print(arr1[i], end=" ")