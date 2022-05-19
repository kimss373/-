def solution(n):
    a = [i for i in range(1,n+1,2) if n % i == 0]

    return len(a)

print(solution(18))