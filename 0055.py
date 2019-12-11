class Solution:
    def canJump(self, nums):
        n = len(nums)
        if n <= 1: return True
        idx = 0
        for i in range(0,n):
            if idx < i:
                return False
            idx = max(idx, i+nums[i])
        return True
    
