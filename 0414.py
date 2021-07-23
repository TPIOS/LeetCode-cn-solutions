class Solution:
    def thirdMax(self, nums):
        res = sorted(list(set(nums)))[::-1]
        if len(res) < 3:
            return res[0]
        else:
            return res[2]

a = Solution()
print(a.thirdMax([1,2]))