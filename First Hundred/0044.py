class Solution:
    def isMatch(self, s, p):
        s_len = len(s)
        p_len = len(p)
        dp = [False] * (s_len+1)
        dp[0] = True

        for i in range(1, p_len+1):
            if p[i-1] != '*':
                for j in range(s_len, 0, -1):
                    dp[j] = dp[j-1] and (p[i-1]=='?' or s[j-1] == p[i-1])
            else:
                idx = 0
                while idx <= s_len and (not dp[idx]): idx += 1
                while idx <= s_len:
                    dp[idx] = True
                    idx += 1
            
            dp[0] = dp[0] and p[i-1] == '*'

        return dp[s_len]

s = Solution()
print(s.isMatch(s = "acdcb", p = "a*c?b"))