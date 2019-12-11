class Solution:
    def findP(self, nums):
        n = len(nums)
        if n < 2 or nums[0] < nums[n-1]: return 0
        left = 0
        right = n-1
        while right - left > 1:
            if nums[left] == nums[right]:
                left += 1
                continue
            mid = left + (right - left) // 2
            if nums[mid] >= nums[left]:
                left = mid
            else:
                right = mid
        
        return right

    def search(self, nums, target):
        n = len(nums)
        if n == 0: return -1
        pivot = self.findP(nums)
        left = pivot
        right = pivot + n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target < nums[mid % n]:
                right = mid - 1
            elif target > nums[mid % n]:
                left = mid + 1
            else:
                return mid % n
        
        return -1

s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))    