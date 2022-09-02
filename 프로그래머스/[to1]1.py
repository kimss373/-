def solution(a):
    stack = []
    result = []
    for i in a:
        stack.append(i)
        if len(stack)>=3:
            if stack[-1] == stack[-2] == stack[-3]:
                tmp = ''
                for _ in range(3):
                    tmp += stack.pop()

                result.append(int(tmp))

    if result:
        return max(result)
    else:
        return -1

print(solution("000111222333444555666777888999"))
print(solution("0"))
print(solution("1111111112222222233333"))
print(solution("9999999999555512334664"))