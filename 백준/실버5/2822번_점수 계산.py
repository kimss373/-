answer = []
result = 0
for i in range(1, 9):
    answer.append([int(input()), i])

answer.sort(key = lambda x : x[0])

xx = []
for i in range(3, 8):
    result += answer[i][0]
    xx.append(answer[i][1])
xx.sort()
print(result)

for i in xx:
    print(i, end=" ")