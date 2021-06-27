class Solution:
    def subsets(self, nums):
        n = len(nums)
        if n == 0: return [[]]
        res = []
        for i in range(1<<n):
            tmp = []
            for j in range(n):
                if i & (1<<j):
                    tmp.append(nums[j])
            res.append(tmp)
        return res

s = Solution()
print(s.subsets([1,2,3]))