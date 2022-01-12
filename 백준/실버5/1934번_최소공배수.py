t = int(input())  # 테스트케이스 개수

import math
for i in range(t):
    a, b = map(int, input().split())
    print(math.lcm(a, b))
