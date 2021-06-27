# class Solution:
#     def maxSubArray(self, nums):
#         n = len(nums)
#         if n == 0: return 0
#         res = nums[0]
#         for i in range(0,n):
#             res = max(res, nums[i])
#         if res <= 0: return res
#         sub_sum = 0
#         res = 0
#         for i in range(0, n):
#             sub_sum += nums[i]
#             sub_sum = max(sub_sum, 0)
#             res = max(res, sub_sum)
#         return res

# s = Solution()
# print(s.maxSubArray([2,1,-2,-1,2,1,-2,-1]))


class Solution:
    def solve(self, a, left, right):
        if left == right: return a[left]
        mid = (left + right) // 2
        maxLeft = self.solve(a, left, mid)
        maxRight = self.solve(a, mid+1, right)
        leftSum = a[mid]
        rightSum = a[mid+1]

        tmpSum = a[mid]
        for i in range(mid-1, left-1, -1):
            tmpSum += a[i]
            # tmpSum = max(tmpSum, 0)
            leftSum = max(leftSum, tmpSum)
        
        tmpSum = a[mid+1]
        for i in range(mid+2, right+1):
            tmpSum += a[i]
            # tmpSum = max(tmpSum, 0)
            rightSum = max(rightSum, tmpSum)
        
        return max(maxLeft, maxRight, leftSum+rightSum)

    def maxSubArray(self, nums):
        if len(nums) == 0: return 0
        return self.solve(nums, 0, len(nums)-1)

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))