class Solution:
    def __init__(self):
        self.cnt = 0
        self.upperlimit = 0

    def queen(self, a, b, c):
        if b == self.upperlimit:
            self.cnt += 1
            return
        d = self.upperlimit & (~(a|b|c))
        while(d):
            bit = d & (~d + 1)
            d -= bit
            self.queen((a|bit)<<1, b|bit, (c|bit)>>1)

    def totalNQueens(self, n):
        self.upperlimit = (1<<n) - 1
        self.queen(0,0,0)
        return self.cnt

s = Solution()
print(s.totalNQueens(4))