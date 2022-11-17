class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        dict = {}
        for i in magazine:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        for i in ransomNote:
            if i in dict:
                if dict[i] == 0:
                    return False
                else:
                    dict[i] -= 1
            else:
                return False
        return True
