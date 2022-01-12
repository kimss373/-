t = int(input())

a = list(map(int, input().split()))
a.sort()

import math
if len(a) == 1:
    print(a[0]**2)
else:
    if math.lcm(a[-1], a[-2]) in a:
        print(math.lcm(a[-1], a[-2])*a[0])
    else:
        print(math.lcm(a[-1], a[-2]))