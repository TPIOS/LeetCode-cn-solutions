class Solution:
    def getMoneyAmount(self, n):
        dp = [[0 for j in range(n+2)] for i in range(n+2)]
        for j in range(1, n+1):
            for i in range(j-1, 0, -1):
                dp[i][j] = float('inf')
                for k in range(i, j+1):
                    dp[i][j] = min(dp[i][j], k+max(dp[i][k-1], dp[k+1][j]))

        return dp[1][n]

a = Solution()
print(a.getMoneyAmount(16))
            