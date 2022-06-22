direct = [[1, 0], [0, 1], [-1, -1]]
def solution(n):
    answer = []
    snail = []
    for i in range(1, n+1):
        arr = [0 for _ in range(i)]
        snail.append(arr)
    snail[0][0] = 1
    if n == 1:
        return [1]
    now = [0, 0]
    nowdirect = 0
    num = 2
    while True:
        a, b = now
        if nowdirect == 0:
            if a + 1<n:
                if snail[a+1][b] == 0:
                    now = [a+1, b]
                    snail[a+1][b] = num
                    num += 1
                else:
                    nowdirect = 1
                    if snail[a][b + 1] != 0:
                        break

            else:
                nowdirect = 1
                if snail[a][b+1] != 0:
                    break

        elif nowdirect == 1:
            if b + 1 < n:
                if snail[a][b+1] == 0:
                    now = [a, b+1]
                    snail[a][b+1] = num
                    num += 1
                else:
                    nowdirect = 2
                    if snail[a - 1][b - 1] != 0:
                        break
            else:
                nowdirect = 2
                if snail[a-1][b-1] != 0:
                    break

        else:
            if 0<= a-1:
                if snail[a-1][b-1] == 0:
                    now = [a-1, b-1]
                    snail[a-1][b-1] = num
                    num += 1
                else:
                    nowdirect = 0
                    if snail[a + 1][b] != 0:
                        break
            else:
                nowdirect = 0
                if snail[a+1][b] != 0:
                    break
    for i in snail:
        answer += i

    return answer

print(solution(1))