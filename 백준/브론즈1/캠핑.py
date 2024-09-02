idx = 1
while True:
    cnt = 0
    L, P, V = map(int, input().split())

    if L == 0 and P == 0 and V == 0:
        break

    cnt += (V // P) * L
    if V % P >= L:
        cnt += L
    else:
        cnt += V % P
    print("Case {0}: {1}".format(idx, cnt))
    idx += 1