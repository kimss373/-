def solution(arr):
    n = max(arr)
    while True:
        cnt = 0
        for i in arr:
            if n % i != 0:
                break
            else:
                cnt += 1
        if cnt == len(arr):
            break
        n += 1

    return n
print(solution([2, 6, 8, 14]))