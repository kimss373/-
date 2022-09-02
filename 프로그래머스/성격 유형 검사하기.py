def solution(survey, choices):
    answer = ''
    nbti = {}
    nbti["R"] = 0
    nbti["T"] = 0
    nbti["C"] = 0
    nbti["F"] = 0
    nbti["J"] = 0
    nbti["M"] = 0
    nbti["A"] = 0
    nbti["N"] = 0

    for i in range(len(survey)):
        tmp = survey[i]
        if choices[i] == 1:
            nbti[tmp[0]] += 3

        elif choices[i] == 2:
            nbti[tmp[0]] += 2

        elif choices[i] == 3:
            nbti[tmp[0]] += 1

        elif choices[i] == 5:
            nbti[tmp[1]] += 1

        elif choices[i] == 6:
            nbti[tmp[1]] += 2

        elif choices[i] == 7:
            nbti[tmp[1]] += 3

    if nbti["R"]>=nbti["T"]:
        answer += "R"
    else:
        answer += "T"

    if nbti["C"] >= nbti["F"]:
        answer += "C"
    else:
        answer += "F"

    if nbti["J"]>=nbti["M"]:
        answer += "J"
    else:
        answer += "M"

    if nbti["A"]>=nbti["N"]:
        answer += "A"
    else:
        answer += "N"
    return answer