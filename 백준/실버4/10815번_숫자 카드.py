#  https://www.acmicpc.net/submit/10815
m = int(input())

m_card = list(map(int, input().split()))

n = int(input())
n_card = list(map(int, input().split()))

diction = {}
for i in n_card:
    diction[i] = 0

for j in m_card:
    if j in diction:
        diction[j] = diction[j]+1

for key in diction:
    print(diction[key], end=" ")