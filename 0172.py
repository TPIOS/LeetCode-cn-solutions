class Solution:
    def trailingZeroes(self, n):
        if n <= 0: return 0 
        num5 = 0
        temp = n
        while temp // 5 > 0:
            num5 += temp // 5
            temp //= 5
        return num5

a = Solution()
print(a.trailingZeroes(0))