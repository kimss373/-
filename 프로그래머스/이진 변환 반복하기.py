def to2(x, cnt):
    result = x
    answer = []
    while result >= 1:
        if result%2 == 1:
            answer.append(str(result%2))
        else:
            cnt += 1
        result //= 2

    return [len(answer), cnt]


def solution(s):
    slist = list(s)
    a = [slist.count("1"), len(slist)-slist.count("1")]
    cnt = 0
    while a[0]>=2:
        cnt += 1
        a = to2(a[0], a[1])

    return [cnt+1, a[1]]

print(solution("110010101001"))
