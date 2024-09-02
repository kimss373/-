n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(str, input().split())))

f = sorted(arr, key=lambda x : (int(x[3]), int(x[2]), int(x[1])))
print(f[-1][0])
print(f[0][0])