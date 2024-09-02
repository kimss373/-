s, d, i, l, n = map(int, input().split())
if n * 4 <= s + d+i+l:
    print(0)
else:
    print(n*4 - (s+d+i+l))
