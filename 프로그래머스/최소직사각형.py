def solution(sizes):
    answer = 0
    choidae = 0
    choiso = 0
    for i in sizes:
        a, b = i
        if a>=b:
            if choidae < a:
                choidae = a
            if choiso < b:
                choiso = b
        else:
            if choidae < b:
                choidae = b
            if choiso < a:
                choiso = a
    answer = choiso * choidae
    return answer