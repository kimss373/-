import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    numberlist = []
    n = int(input())
    for i in range(n):
        numberlist.append(str(input().strip()))

    numberlist.sort()

    answer = "YES"
    for i in range(len(numberlist)-1):
        if len(numberlist[i])<len(numberlist[i+1]):
            if numberlist[i+1][:len(numberlist[i])] == numberlist[i]:
                answer = "NO"
                break

    print(answer)

