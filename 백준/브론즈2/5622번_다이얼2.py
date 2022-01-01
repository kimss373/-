a = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
count = 0
b=input()
for i in range(len(b)):
    for j in a:
        if b[i] in j:
            count += a.index(j) + 3
print(count)