class Solution:
    def allCellsDistOrder(self, R, C, r0, c0):
        matrix = []
        for i in range(R):
            for j in range(C):
                matrix.append([i,j])
        res = sorted(matrix, key = lambda x: abs(x[0]-r0)+abs(x[1]-c0))
        return res

a = Solution()
print(a.allCellsDistOrder(R = 2, C = 3, r0 = 1, c0 = 2))