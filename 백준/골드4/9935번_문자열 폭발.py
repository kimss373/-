a = list(input())
b = list(input())
x = len(b)
stack = []

for i in range(len(a)):
    stack.append(a[i])

    if stack[-1] == b[-1] and len(stack) >= x:
        if stack[len(stack)-x:] == b:
            for _ in range(x):
                stack.pop()

answer = ''
if stack:
    for i in stack:
        answer += i

else:
    answer = "FRULA"

print(answer)