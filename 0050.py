class Solution:
    def myPow(self, x, n):
        if x == 0 or x == 1: return x
        if n == 0: return 1.0
        if n == -n: 
            y = self.myPow(x, n//2)
            return y * y
        if n < 0: return 1 / self.myPow(x, -n)
        y = self.myPow(x, n//2)
        res = y * y
        if n % 2 == 1: res *= x
        return res

a = Solution()
print(a.myPow(2.0, 10))