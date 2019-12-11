class Solution:
    def removeDuplicates(self, nums):
        l = len(nums)
        if l <= 2: return l
        idx = 2
        while idx < l:
            if nums[idx-2] == nums[idx]:
                nums.remove(nums[idx])
                l -= 1
            else:
                idx += 1
        
        return l

s = Solution()
print(s.removeDuplicates([1,2,2,2]))
