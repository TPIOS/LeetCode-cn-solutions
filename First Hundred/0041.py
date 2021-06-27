class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(0,n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = n + 1
                #preprocess
        
        for i in range(0,n):
            val = abs(nums[i])
            if val == n + 1: continue
            if nums[val-1] > 0: nums[val-1] = -nums[val-1] 
            #negative number represents that its (index number + 1) has been found.
        
        idx = 0
        while idx < n:
            if nums[idx] > 0: break
            idx += 1
        
        return idx + 1