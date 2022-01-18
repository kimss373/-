n = int(input())                        # 배열 길이 입력
a = list(map(int, input().split()))     # 배열 a 입력
b = list(map(int, input().split()))     # 배열 b 입력

s=0
for i in range(n):
    s += min(a) * max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))

print(s)