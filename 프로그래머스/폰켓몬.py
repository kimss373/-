def solution(nums):
    answer = 0
    x = len(nums) // 2
    y = len(list(set(nums)))
    if y >= x:
        return x
    else:
        return y