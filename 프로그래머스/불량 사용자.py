from itertools import permutations
def check(userlist, banlist):
    for i in range(len(userlist)):
        if len(userlist[i]) != len(banlist[i]):
            return False
        for j in range(len(banlist[i])):
            if banlist[i][j] == '*':
                continue
            elif userlist[i][j] != banlist[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    answer = []
    for i in permutations(user_id, len(banned_id)):
        if check(i, banned_id):
            z = set(i)
            if z not in answer:
                answer.append(z)
    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))