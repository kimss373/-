def solution(brown, yellow):
    answer = []

    while True:
        height = 1
        if yellow % height == 0:
            if brown - 2*((yellow//height) + height) == 4:
                break

    answer.append((brown+yellow)//(height+2))
    answer.append(height+2)

    return answer

print(solution(8, 1))