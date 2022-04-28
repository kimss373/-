def solution(s):
    stack = [s[0]]
    for i in s[1:]:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    if stack:
        return 0
    elif not stack:
        return 1
