a, b, v = map(int, input().split())  # a, b, v 입력
if (v-a)%(a-b) == 0:
    print((v-a)//(a-b)+1)
else:
    print((v - a) // (a - b) + 2)

