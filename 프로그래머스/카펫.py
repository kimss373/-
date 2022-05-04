def solution(brown, yellow):
    answer = []
    height = 1

    while True:
        if yellow % height == 0:
            if brown - 2*((yellow//height) + height) == 4:
                break
        height += 1

    answer.append((brown+yellow)//(height+2))
    answer.append(height+2)

    return answer

print(solution(24, 24))