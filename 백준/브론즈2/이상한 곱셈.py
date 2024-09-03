a, b = map(str, input().split())

a_sum = 0

for i in a:
    a_sum += int(i)

sum = 0
for i in b:
    sum += a_sum * int(i)

print(sum)

