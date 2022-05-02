def solution(fees, records):
    answer = []
    carnum = []
    time = {}

    for i in records:
        x = int(i[6:10])
        if x not in carnum:
            carnum.append(x)
    carnum.sort()
    for i in carnum:
        x = str(i)
        while len(x)!= 4:
            x = '0' + x

        time[x] = [0]

    for i in records:
        info = i.split()
        hour, minute = int(info[0][:2]), int(info[0][3:5])

        if info[2] == 'IN':
            if info[1] in time:
                time[info[1]] = [time[info[1]][0], 60*hour+minute, 23*60+59]

        else:
            time[info[1]][0] += 60*hour + minute - time[info[1]][1]
            time[info[1]][1] = 60*hour + minute
            time[info[1]][2] = 60*hour + minute

    for i in time:
        use = time[i][0] + time[i][2] - time[i][1]

        a = fees[0]-use
        if a >=0:
            price = fees[1]
        else:
            a = a*-1
            if a%fees[2] != 0:
                price = fees[1] + (a//fees[2]+1)*fees[3]
            else:
                price = fees[1] + (a//fees[2])*fees[3]

        answer.append(price)
    return answer
print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))