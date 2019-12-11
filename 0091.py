class Solution:
    def numDecodings(self, s):
        n = len(s)
        d = [1]+[0]*n
        if s[0] == '0':
            d[1] = 0
        else:
            d[1] = 1
        for i in range(1,n):
            if s[i] != '0': d[i+1] += d[i]
            if s[i-1] != '0' and (s[i-1]+s[i]) <= '26': d[i+1] += d[i-1]
        return d[n]

s = Solution()
print(s.numDecodings('226'))