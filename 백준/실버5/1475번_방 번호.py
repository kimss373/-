n=list(map(int, input()))

a = []  # 0~9순으로 n에 몇개나 있는지 적어놓는 리스트
for i in range(10):
    a.append(n.count(i))

a[6] = a[6]+a[9]
a.pop(9)

if a[6] % 2 == 0:
    a[6] = a[6] //2
else:
    a[6] = a[6] //2 +1
print(max(a))