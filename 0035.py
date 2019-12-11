class Solution:
    def searchLeft(self, nums, target, left, right):
        while left <= right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

    def searchInsert(self, nums, target):
        n = len(nums)
        idx = self.searchLeft(nums, target, 0, n-1)
        return idx

