class Solution(object):
    def romanToInt(self, s):
        answer = 0
        dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        ox = 0
        tmp = 0
        minus = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                if tmp != 0:
                    answer += tmp + dict[s[i]]
                elif minus != 0:
                    answer += dict[s[i]] - minus
                else:
                    answer += dict[s[i]]
                break

            if dict[s[i]] > dict[s[i + 1]]:
                if ox == 1:
                    tmp += dict[s[i]]
                    answer += tmp
                    tmp = 0
                    ox = 0
                    continue
                answer += dict[s[i]] - minus
                minus = 0

            elif dict[s[i]] < dict[s[i + 1]]:
                minus += dict[s[i]]
            elif dict[s[i]] == dict[s[i + 1]]:
                ox = 1
                tmp += dict[s[i]]

        return answer