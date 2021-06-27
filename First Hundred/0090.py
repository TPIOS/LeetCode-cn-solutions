class Solution:
    def __init__(self):
        self.res = []
    def make(self, index, path, n, nums):
        self.res.append(path[:])
        if index > n: return
        for i in range(index, n):
            if i > index and nums[i] == nums[i-1]: continue
            self.make(i+1, path+[nums[i]], n, nums)
    def subsetsWithDup(self, nums):
        nums.sort()
        self.make(0,[],len(nums),nums)
        return self.res
s = Solution()
print(s.subsetsWithDup([1,2,2]))
