def solution(phone_book):
    diction = {}
    answer = True
    for i in phone_book:        # 딕셔너리에 키값 추가
        diction[i] = 0

    for j in phone_book:
        number = ""
        for k in j:         # number에 phone_book의 글자 하나씩 추가하며 딕셔너리에 있는지 검사
            number += k
            if number in diction and number != j:       # 딕셔너리에 있으며 딕셔너리 안의 값이 자기 자신이 아니면 False
                return False

    return answer       # 다 검사하고 아무일도 일어나지 않으면 True
print(solution(["123","456","789"]))