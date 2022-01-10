n, m = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]

def B_reverse(a, b, c):
    count = 0
    for i in range(a, a+8, 2):
        for j in range(b, b+8, 2):
            if c[i][j] != 'B':
                count += 1
    for k in range(a, a + 8, 2):
        for l in range(b + 1, b + 8, 2):
            if c[k][l] != 'W':
                count += 1
    for o in range(a+1, a + 8, 2):
        for p in range(b, b + 8, 2):
            if c[o][p] != 'W':
                count += 1
    for y in range(a+1, a + 8, 2):
        for u in range(b + 1, b + 8, 2):
            if c[y][u] != 'B':
                count += 1
    return count

def W_reverse(a, b, c):
    count = 0
    for i in range(a, a+8, 2):
        for j in range(b, b+8, 2):
            if c[i][j] != 'W':
                count += 1
    for k in range(a, a + 8, 2):
        for l in range(b + 1, b + 8, 2):
            if c[k][l] != 'B':
                count += 1
    for o in range(a+1, a + 8, 2):
        for p in range(b, b + 8, 2):
            if c[o][p] != 'B':
                count += 1
    for y in range(a+1, a + 8, 2):
        for u in range(b + 1, b + 8, 2):
            if c[y][u] != 'W':
                count += 1
    return count
count_list = []

for q in range(0, n-8+1):
    for w in range(0, m-8+1):
        count_list.append(B_reverse(q, w, arr))
        count_list.append(W_reverse(q, w, arr))

print(min(count_list))