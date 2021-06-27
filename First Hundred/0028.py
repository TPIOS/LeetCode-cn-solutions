class Solution:
    def __init__(self):
        self.nxt = []

    def makeNext(self, m, needle):
        k = 0
        for i in range(1,m):
            while k > 0 and needle[i] != needle[k]:
                k = self.nxt[k-1]
            if needle[i] == needle[k]:
                k += 1

            self.nxt[i] = k
            
    def strStr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)
        if m == 0: return 0
        self.nxt = [0]*m
        self.makeNext(m, needle)
        q = 0
        for i in range(n):
            while q > 0 and needle[q] != haystack[i]:
                q = self.nxt[q-1]
            if needle[q] == haystack[i]:
                q += 1

            if q == m:
                return i-m+1

        return -1

s = Solution()
print(s.strStr("aaaaa","bl"))