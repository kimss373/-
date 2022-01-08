a=list(input())
for i in range(0, len(a)-1):
    max_index = i
    for j in range(i+1, len(a)):
        if a[j]>a[max_index]:
            max_index=j
    a[i], a[max_index] = a[max_index], a[i]
for k in a:
    print(k, end="")