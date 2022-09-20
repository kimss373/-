class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        if x[0] == '-':
            return False

        for i in range(len(x) // 2):
            if x[i] != x[len(x) - i - 1]:
                return False
        return True

#
# class Solution(object):
#     def isPalindrome(self, x):
#         x = list(str(x))
#         return x == x[::-1]