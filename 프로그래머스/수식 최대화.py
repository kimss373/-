yeonsan = [['*', '+', '-'], ['*', '-', '+'], ['+', '-', '*'], ['+', '*', '-'], ['-', '*', '+'], ['-', '+', '*']]
def solution(expression):
    answer = []
    tmp = ''
    result = []
    for i in expression:
        if i =='-' or i=='+' or i=='*':
            result.append(int(tmp))
            result.append(i)
            tmp= ''

        else:
            tmp += i
    result.append(int(tmp))

    for j in range(6):
        stack1 = []
        stack2 = []
        stack3 = []
        skip = -1
        for i in range(len(result)):
            if i == skip:
                skip = -1
                continue
            if result[i] == yeonsan[j][0]:
                if yeonsan[j][0] == '*':
                    stack1.append(stack1.pop()*result[i+1])
                    skip = i+1
                elif yeonsan[j][0] == '-':
                    stack1.append(stack1.pop()-result[i+1])
                    skip = i+1
                elif yeonsan[j][0] == '+':
                    stack1.append(stack1.pop()+result[i+1])
                    skip = i+1
            else:
                stack1.append(result[i])

        for k in range(len(stack1)):
            if k == skip:
                skip = -1
                continue
            if stack1[k] == yeonsan[j][1]:
                if yeonsan[j][1] == '*':
                    stack2.append(stack2.pop() * stack1[k+1])
                    skip = k + 1
                elif yeonsan[j][1] == '-':
                    stack2.append(stack2.pop() - stack1[k + 1])
                    skip = k + 1
                elif yeonsan[j][1] == '+':
                    stack2.append(stack2.pop() + stack1[k + 1])
                    skip = k + 1
            else:
                stack2.append(stack1[k])

        for v in range(len(stack2)):
            if v == skip:
                skip = -1
                continue
            if stack2[v] == yeonsan[j][2]:
                if yeonsan[j][2] == '*':
                    stack3.append(stack3.pop() * stack2[v+1])
                    skip = v + 1
                elif yeonsan[j][2] == '-':
                    stack3.append(stack3.pop() - stack2[v + 1])
                    skip = v + 1
                elif yeonsan[j][2] == '+':
                    stack3.append(stack3.pop() + stack2[v + 1])
                    skip = v + 1
            else:
                stack3.append(stack2[v])



        answer.append(abs(stack3[0]))

    return max(answer)

print(solution("100-200*300-500+20"))