def solution(genres, plays):
    answer = []
    dict = {}
    record = []
    for i in range(len(genres)):
        if genres[i] in dict:
            dict[genres[i]][1].append([plays[i], i])
            dict[genres[i]][0]+=plays[i]
        else:
            dict[genres[i]] = [plays[i], [[plays[i], i]]]
    for i in dict:
        record.append([dict[i][0], i])
        dict[i][1] = sorted(dict[i][1], key=lambda x:-x[0])

    record_sort = sorted(record, key=lambda x:-x[0])

    for i in range(len(record_sort)):
        if len(dict[record_sort[i][1]][1]) == 1:
            answer.append(dict[record_sort[i][1]][1][0][1])
        else:
            for j in range(2):
                answer.append(dict[record_sort[i][1]][1][j][1])

    print("dict = ", dict)
    print("record_sort = ", record_sort)

    return answer
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))