def solution(arr):
    answer = []
    min = 50000
    idx = 0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            idx = i
        answer.append(arr[i])
    if answer:
        answer.pop(idx)
    if not answer:
        return [-1]
    else:
        return answer

print(solution([4,3,2,1]))