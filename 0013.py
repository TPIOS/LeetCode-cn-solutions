class Solution:
    def romanToInt(self, s):
        d = {
                'I' : 1,
                'V' : 5,
                'X' : 10,
                'L' : 50,
                'C' : 100,
                'D' : 500,
                'M' : 1000,
            }
        n = len(s)
        res = 0
        idx = 0
        while idx < n:
            if idx < n-1 and d[s[idx]] < d[s[idx+1]]:
                res -= d[s[idx]]
                res += d[s[idx+1]]
                idx += 2
            else:
                res += d[s[idx]]
                idx += 1
        
        return res

s = Solution()
print(s.romanToInt("IV"))