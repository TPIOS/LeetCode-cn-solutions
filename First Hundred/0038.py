class Solution:
    def nxt(self, s):
        ss = ""
        n = len(s)
        i = 0
        while i < n:
            tmp = i + 1
            while tmp < n and s[tmp] == s[i]: tmp += 1
            ss += str(tmp - i) + s[i]
            i = tmp

        return ss

    def countAndSay(self, n):
        res = ['1']
        for i in range(1, n):
            res.append(self.nxt(res[-1]))
        
        return res[-1]

s = Solution()
print(s.countAndSay(5))