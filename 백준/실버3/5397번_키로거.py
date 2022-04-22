t = int(input())
for i in range(t):
    cmd = list(input())
    left = []
    right = []
    for j in cmd:
        if j== ">":
            if right:
                left.append(right.pop())
        elif j=="<":
            if left:
                right.append(left.pop())
        elif j=='-':
            if left:
                left.pop()
        else:
            left.append(j)

    print("".join(left)+ "".join(reversed(right)))

