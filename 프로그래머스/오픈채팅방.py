def solution(record):
    answer = []
    dict = {}
    for i in record:
        if i[:5] == "Enter" or i[:5] == "Chang":
            command, userid, nickname = i.split()
            dict[userid] = nickname



    for j in record:
        if j[:5] == "Enter":
            command, userid, nickname = j.split()
            answer.append("{}님이 들어왔습니다.".format(dict[userid]))
        elif j[:5] == "Leave":
            command, userid = j.split()
            answer.append("{}님이 나갔습니다.".format(dict[userid]))
    return answer

#   print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))