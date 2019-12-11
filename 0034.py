# class Solution:
#     def searchRange(self, nums, target):
#         try:
#             return [nums.index(target), len(nums)-1-nums[::-1].index(target)]
#         except:
#             return [-1, -1]

class Solution:
    def searchLeft(self, nums, target, left, right):
        while left <= right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left


    def searchRange(self, nums, target):
        n = len(nums)
        idx1 = self.searchLeft(nums, target, 0, n-1)
        idx2 = self.searchLeft(nums, target+1, 0, n-1) - 1

        if idx1 < n and nums[idx1] == target:
            return [idx1, idx2]
        else:
            return [-1, -1]

s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))