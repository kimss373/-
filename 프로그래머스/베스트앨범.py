def solution(genres, plays):
    answer = []
    diction = {}
    for x in zip(genres, plays):
        if x[0] in diction:
            diction[x[0]] += x[1]
        else:
            diction[x[0]] = x[1]
    print(diction)
    return answer
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))