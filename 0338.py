class Solution:
    def countOne(self, n):
        ans = 0
        while n != 0:
            if n % 2 == 0:
                n = n // 2
            else:
                ans = ans + 1
                n = n - 1
        return ans
    def countBits(self, n):
        ret = []
        for i in range(0, n + 1):
            ret.append(self.countOne(i))
        return ret

a = Solution()
print(a.countBits(5))