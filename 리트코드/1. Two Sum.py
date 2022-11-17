class Solution(object):
    def twoSum(self, nums, target):
        tmp = []
        for i in range(len(nums)):
            if nums[i] in tmp:
                return [tmp.index(nums[i]), i]
            tmp.append(target-nums[i])

