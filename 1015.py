class Solution:
    def smallestRepunitDivByK(self, k):
        if k%2 == 0 or k%5 == 0: return -1
        ans = 1
        mod = 1
        while True:
            mod = mod % k
            if mod == 0:
                return ans
            else:
                ans += 1
                mod = mod*10 + 1
        return ans