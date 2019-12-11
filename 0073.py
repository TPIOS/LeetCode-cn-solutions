class Solution:
    def setZeroes(self, matrix):
        n = len(matrix)
        if n == 0: return
        m = len(matrix[0])
        if m == 0: return
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for k in range(n):
                        if matrix[k][j] != 0: matrix[k][j] = '0'
                    for k in range(m):
                        if matrix[i][k] != 0: matrix[i][k] = '0'
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    matrix[i][j] = 0
        