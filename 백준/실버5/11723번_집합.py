import sys
m = int(sys.stdin.readline())
check_dict = {}
for w in range(1, 21):
    check_dict[str(w)] = 1
y = check_dict

for k in range(1, 21):
    check_dict[str(k)] = 0
x = check_dict

for _ in range(m):
    a = tuple(sys.stdin.readline().split())
    print(a)
    if a[0] == 'add':
        if check_dict[a[1]] != 0:
            continue
        else:
            check_dict[a[1]] = 1

    elif a[0] == 'remove':
        if check_dict[a[1]] != 0:
            check_dict[a[1]] = 0
        else:
            continue

    elif a[0] == 'check':
        if check_dict[a[1]] != 0:
            print(1)
        else:
            print(0)

    elif a[0] == 'toggle':
        if check_dict[a[1]] != 0:
            check_dict[a[1]] = 0
        else:
            check_dict[a[1]] = 1
    elif a[0] == 'all':
        for j in range(1, 21):
            check_dict = y
    elif a[0] == 'empty':
        for l in range(1, 21):
            check_dict = x