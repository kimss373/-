n = int(input())
top = list(map(int, input().split()))
stack = [[1e9, 0], [top[0], 1]]
print(0, end=" ")
for i in range(1, n):
    while stack[-1][0]<top[i]:
        stack.pop()
    print(stack[-1][1], end=" ")
    stack.append([top[i], i+1])