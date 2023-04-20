def solution(players, callings):

    play = {player: i for i, player in enumerate(players)}
    rank = {i: player for i, player in enumerate(players)}

    for i in callings:
        idx = play[i]
        name = rank[idx - 1]

        rank[idx] = name
        rank[idx - 1] = i

        play[name] = idx
        play[i] = idx - 1

    return list(rank.values())

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))