import sys
input = sys.stdin.readline
dict = {}
cnt = 0
n = int(input())
x = 1
for i in range(n):
    dict[input().rstrip()] = x
    x+=1

daegi = [i for i in range(1, n+1)]
passs = []
for i in range(n):
    z = input().rstrip()
    if dict[z] > daegi[0]:
        passs.append(dict[z])
        cnt += 1
    elif dict[z] == daegi[0]:
        daegi.pop(0)
        if passs:
            passs.sort()
            while True:
                if passs[0] == daegi[0]:
                    daegi.pop(0)
                    passs.pop(0)
                    if not passs or not daegi:
                        break
                else:
                    break


print(cnt)