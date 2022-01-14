s=int(input())

a = 0
i = 0
while a<s:
    i += 1
    a += i
if a == s:
    print(i)
else:
    print(i-1)