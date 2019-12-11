class Solution:
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        if n == 0: return False
        m = len(matrix[0])
        if m == 0: return False
        left = 0
        right = n*m - 1
        while left <= right:
            mid = (left + right) // 2
            if target < matrix[mid//m][mid%m]:
                right = mid - 1
            elif target == matrix[mid//m][mid%m]:
                return True
            else:
                left = mid + 1
        
        return False
