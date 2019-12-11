class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        if n == 0 or n == 1: return
        for i in range(0, (n+1)//2):
            for j in range(0, n//2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = tmp