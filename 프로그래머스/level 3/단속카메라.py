def solution(routes):
    answer = 0
    routes.sort(key=lambda x: [x[1], x[0]])

    e = -30001

    for i in routes:
        if i[0] > e:
            answer += 1
            e = i[1]

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))