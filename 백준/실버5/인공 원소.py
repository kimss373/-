n = int(input())

arr = [2, 3, 5, 7]

for i in range(11, 119):
    isPrime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        arr.append(i)

for i in range(n):
    tmp = int(input())
    answer = "No"
    sum = 0
    for j in range(len(arr)):
        sum += arr[j]
        for k in range(len(arr)):
            sum += arr[k]
            if sum == tmp:
                answer = "Yes"
            sum -= arr[k]
        sum -= arr[j]
    print(answer)
