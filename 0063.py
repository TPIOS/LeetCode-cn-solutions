class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        if n == 0: return 0
        m = len(obstacleGrid[0])
        d = [[0 for col in range(m)] for row in range(n)]
        for i in range(n):
            if obstacleGrid[i][0] != 1:
                d[i][0] = 1
            else:
                break
        for i in range(m):
            if obstacleGrid[0][i] != 1:
                d[0][i] = 1
            else:
                break
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j] != 1:
                    d[i][j] = d[i-1][j] + d[i][j-1]
        
        return d[n-1][m-1]

s = Solution()
print(s.uniquePathsWithObstacles([
  [0,1,0],
  [1,0,0],
  [0,0,0]
]))