roomNum = input()

arr = [0 for i in range(10)]

sixCount = 0
for i in roomNum:
    if i == '6' or i == '9':
        sixCount += 1
    else:
        arr[int(i)] += 1

if sixCount % 2 == 0:
    print(max(sixCount//2, max(arr)))
else:
    print(max(sixCount//2+1, max(arr)))