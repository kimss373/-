import sys
from collections import Counter
n = int(sys.stdin.readline())
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))

a.sort()
# 산술평균
if (sum(a)%n) * 10/n >= 5:
    print(sum(a)//n + 1)
else:
    print(sum(a)//n)

# 중앙값
print(a[(n-1)//2])

# 최빈값
count = Counter(a).most_common(2)

if len(a) >1:
    if count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])
# 범위
print(max(a)-min(a))