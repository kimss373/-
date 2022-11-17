class Solution(object):
    def maximumWealth(self, accounts):
        total = 0
        for i in accounts:
            if total <= sum(i):
                total = sum(i)
        return total