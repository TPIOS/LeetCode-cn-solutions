class Solution:
    def minDistance(self, word1, word2):
        n1 = len(word1)
        n2 = len(word2)
        if n1 < n2:
            n1, n2 = n2, n1
            word1, word2 = word2, word1
        
        dp = [[2 for col in range(n2 + 1)] for row in range(n1 + 1)]
        for i in range(n2+1):
            dp[0][i] = i
        
        f = 1
        nf = (not f) + 0
        for i in range(1,n1+1):
            for j in range(n2+1): dp[f][j] = 0x7fffffff
            dp[f][0] = i
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[f][j] = dp[nf][j-1]
                else:
                    dp[f][j] = min(dp[nf][j], dp[f][j-1]) + 1
                    dp[f][j] = min(dp[f][j], dp[nf][j-1] + 1)

            f = (not f) + 0
            nf = (not f) + 0
        
        return dp[nf][n2]
