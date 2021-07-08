import numpy as np
class Solution:
    def transpose(self, matrix):
        matrixTrue = np.array(matrix)
        matrixTrue = matrixTrue.T
        resMatrix = []
        for row in matrixTrue:
            resMatrix.append([])
            for num in row:
                resMatrix[-1].append(int(num))
                
        return resMatrix

a = Solution()
print(a.transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]]))