def solution(A,B):
    answer = 0
    sorted_A = list(sorted(A))
    sorted_B = list(reversed(sorted(B)))

    for i in range(len(A)):
        answer += sorted_A[i] * sorted_B[i]

    return answer

print(solution([1, 4, 2], [5, 4, 4]))