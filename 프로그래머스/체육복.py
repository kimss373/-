def solution(n, lost, reserve):

    reserve_unique = set(reserve) - set(lost)
    lost_unique = set(lost) - set(reserve)
    for r in reserve_unique:
        f = r-1
        b = r+1
        if f in lost_unique:
            lost_unique.remove(f)
        elif b in lost_unique:
            lost_unique.remove(b)


    return n-len(lost_unique)