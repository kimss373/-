arr = [[1, 0, 0, 0, 0, 0, 0,0,0,0, 0,0,0,0,0] for _ in range(14)]
arr.insert(0,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

for i in range(1, 15):
    for j in range(1, 15):
        arr[i][j] = arr[i-1][j]+arr[i][j-1]

t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    print(arr[k][n-1])