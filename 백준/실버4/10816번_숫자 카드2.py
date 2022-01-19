from collections import Counter
m = int(input())

m_card = list(map(int, input().split()))

n = int(input())

n_card = list(map(int, input().split()))

counter = Counter(m_card)

for i in n_card:
    print(counter[i], end=" ")
