class Solution:
    def __init__(self):
        self.res = list()

    def make(self, n, s, l):
        if n == 0:
            s += ")"*l
            self.res.append(s)
            return
        
        if l < n: return

        self.make(n-1, s+"(", l)
        self.make(n, s+")", l-1)

    def generateParenthesis(self, n):
        if n == 0: return []
        self.make(n-1, "(", n)
        return self.res

s = Solution()
print(s.generateParenthesis(3))