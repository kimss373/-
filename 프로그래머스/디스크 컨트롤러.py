def solution(jobs):
    cnt = 0
    time = 0
    realtime = 0
    que = []
    x = len(jobs)
    jobs.sort(key=lambda x : x[0])

    while cnt < x:

        while jobs and jobs[0][0]<=time:
            a, b = jobs.pop(0)
            que.append([a, b])
        que.sort(key = lambda x : x[1])
        if que:
            c, d = que.pop(0)
            time += d
            realtime += time-c
            cnt += 1
        else:
            time += 1

    answer = realtime//x

    return answer

print(solution([[0, 3], [1, 9], [2, 6]]	))