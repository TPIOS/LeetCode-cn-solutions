class Solution:
    def minPathSum(self, grid):
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        if m == 0: return 0
        for i in range(1,m):
            grid[0][i] += grid[0][i-1]
        for i in range(1,n):
            grid[i][0] += grid[i-1][0]
        for i in range(1,n):
            for j in range(1,m):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[n-1][m-1]

s = Solution()
print(s.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))