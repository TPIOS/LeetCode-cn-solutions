class Solution:
    def removeDuplicates(self, nums):
        l = len(nums)
        if l == 0: return 0
        idx = 1
        while idx != l:
            if nums[idx] == nums[idx-1]:
                nums.remove(nums[idx])
                l -= 1
            else:
                idx += 1

        return len(nums)


s = Solution()
print(s.removeDuplicates([1,1,2]))