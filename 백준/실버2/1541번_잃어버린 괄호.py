a = list(input())
x = []
def lnum(number):
    x = 0
    y = 1
    for i in range(len(number) - 1, -1, -1):
        x += int(number[i]) * y
        y *= 10
    return x

end = 0
tmp = 0

for i in range(len(a)):
    if a[i] == '+' or a[i] == '-':
        for _ in range(i):
            x.append(a.pop(0))
        break
if x == []:
    x = a
end += lnum(x)

while True:
    number = []

    sign = a.pop(0)

    for i in range(len(a)):
        if a[i] == '+' or a[i] == '-':
            for _ in range(i):
                number.append(a.pop(0))
            break
    if number == []:
        number = a

    if sign == '+' and tmp == 0:
        end += lnum(number)
    elif sign == '+' and tmp != 0:
        tmp += lnum(number)
    elif sign == '-' and tmp != 0:
        end = end - tmp
        tmp = 0
        tmp += lnum(number)
    elif sign == '-' and tmp == 0:
        tmp += lnum(number)

    if number == a:
        break
print(end-tmp)