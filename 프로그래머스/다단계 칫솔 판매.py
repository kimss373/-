def solution(enroll, referral, seller, amount):
    answer = []
    dict = {}
    for i in range(len(enroll)):
        dict[enroll[i]] = [referral[i], 0]

    for i in range(len(seller)):
        x = seller[i]
        tmp = amount[i] * 100

        while True:
            y = x
            tmp1 = tmp//10
            dict[x][1] += tmp-tmp1
            x = dict[x][0]
            tmp = tmp1
            if x == '-':
                break
            elif tmp1==0:
                break

    for i in enroll:
        answer.append(dict[i][1])

    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))