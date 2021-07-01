class Solution:
    def strangePrinter(self, s):
        strLength = len(s)
        if strLength == 0: return 0
        dp = [[float('inf') for i in range(strLength)] for j in range(strLength)]
        for i in range(strLength):
            dp[i][i] = 1
        for i in range(strLength-1, -1, -1):
            for j in range(i+1, strLength):
                dp[i][j] = 1 + dp[i+1][j]
                for k in range(i+1, j):
                    if s[i] == s[k]:
                        dp[i][j] = min(dp[i][j], dp[i+1][k]+dp[k+1][j])
                if s[i] == s[j]:
                    dp[i][j] = min(dp[i][j], dp[i+1][j])
        return dp[0][-1]

a = Solution()
print(a.strangePrinter("tgbtbg"))