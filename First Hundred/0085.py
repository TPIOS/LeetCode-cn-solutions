class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        if n == 0: return 0
        left = [0]*n
        right = [0]*n
        
        left[0] = 0
        for i in range(1,n):
            left[i] = i
            j = i
            while left[j] - 1 >=0 and heights[left[j]-1] >= heights[i]:
                j = left[j] - 1
            left[i] = left[j]
        
        right[n-1] = n-1
        for i in range(n-2,-1,-1):
            right[i] = i
            j = i
            while right[j] + 1 <= n-1 and heights[right[j] + 1] >= heights[i]:
                j = right[j] + 1
            right[i] = right[j]
        
        res = -1
        for i in range(n):
            res = max(res, heights[i]*(right[i]-left[i]+1))
        
        return res

    def maximalRectangle(self, matrix):
        n = len(matrix)
        if n == 0: return 0
        m = len(matrix[0])
        if m == 0: return 0
        for i in range(m): matrix[0][i] = int(matrix[0][i])
        for i in range(1,n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i-1][j] != 0 and matrix[i][j] != 0:
                    matrix[i][j] = matrix[i-1][j] + 1
        
        res = -1
        for i in range(n):
            res = max(res, self.largestRectangleArea(matrix[i]))

        return res

s = Solution()
print(s.maximalRectangle([
  ["1","0","1","1","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","1","1","0"]
]))                
        