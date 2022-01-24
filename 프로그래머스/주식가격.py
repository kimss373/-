def solution(prices):
    answer = [0]*len(prices)
    stack = []
    for i, j in enumerate(prices):
        while stack and stack[-1][1] > j:
            answer[stack[-1][0]] = i-stack[-1][0]
            stack.pop()
        stack.append((i, j))
    while stack:
        a = stack.pop()
        answer[a[0]] = len(prices) - a[0] - 1

    return answer

a = solution([1, 2, 3, 2, 3])

print(a)