count = 0
for i in range(1, 9):
    a=list(input())
    if i%2 !=0:
        for j in range(0, 8, 2):
            if a[j] =="F":
                count +=1
    else:
        for k in range(1, 9, 2):
            if a[k] == "F":
                count += 1
print(count)