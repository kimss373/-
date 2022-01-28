n = int(input())
numlist = [i for i in range(1, n+1)]

stack = []
plusminus = []
for _ in range(n):
    x = int(input())
    y=1
    while y ==1:
        if numlist and numlist[0] == x:
            numlist.pop(0)
            plusminus.append('+')
            plusminus.append('-')
            y = 0
        elif stack and stack[-1] == x:
            stack.pop()
            plusminus.append('-')
            y = 0
        elif numlist:
            stack.append(numlist.pop(0))
            plusminus.append('+')

        else:
            plusminus.clear()
            plusminus.append('NO')
            y = 0
    if plusminus[0] == 'NO':
        break

for j in range(len(plusminus)):
    print(plusminus[j])