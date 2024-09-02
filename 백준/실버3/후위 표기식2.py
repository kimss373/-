n = int(input())

sick = input()

diction = {}

for i in sick:
    if i == '*' or i == '+' or i == '/' or i == '-':
        continue
    if i not in diction:
        diction[i] = int(input())

stack = []
for i in sick:
    if i != '*' and i != '+' and i != '/' and i != '-':
        stack.append(diction[i])
    else:
        b = stack.pop()
        a = stack.pop()
        if i == '*':
            stack.append(a * b)
        elif i == '+':
            stack.append(a + b)
        elif i == '/':
            stack.append(a / b)
        else:
            stack.append(a - b)

print(f'{stack[0]:.2f}')