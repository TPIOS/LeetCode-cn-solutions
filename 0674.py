class Solution:
    def findLengthOfLCIS(self, nums):
        maxLen = 1
        start = 0
        n = len(nums)
        if n == 0: return 0
        for i in range(n-1):
            if nums[i] >= nums[i+1]:
                tempLen = i - start + 1
                maxLen = max(maxLen, tempLen)
                start = i + 1
        tempLen = n - start
        maxLen = max(maxLen, tempLen)
        return maxLen