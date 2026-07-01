

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        sumrow = []

        for row in mat:
            sumrow.append(sum(row))

        sumcol = [0] * m

        for j in range(m):
            for i in range(n):
                sumcol[j] += mat[i][j]

        ans = 0

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and sumrow[i] == 1 and sumcol[j] == 1:
                    ans += 1

        return ans
