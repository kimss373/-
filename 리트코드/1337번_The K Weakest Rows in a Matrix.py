class Solution(object):
    def kWeakestRows(self, mat, k):
        answer = []
        result = []
        for i in range(len(mat)):
            x = mat[i].count(1)
            result.append([x, i])

        result.sort(key=lambda x: (x[0], x[1]))

        for i in range(k):
            answer.append(result[i][1])

        return answer