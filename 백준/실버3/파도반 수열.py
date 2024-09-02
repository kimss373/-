t = int(input())

arr = [1,1,1]
for i in range(97):
    arr.append(arr[i]+arr[i+1])

for i in range(t):
    n = int(input())
    print(arr[n-1])