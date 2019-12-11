class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        flag = False
        if n <= 1: return
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                flag = True
                break

        if not flag:
            nums[::] = nums[::-1]
            return
        
        for j in range(n-1, i, -1):
            if nums[j] > nums[i]:
                break

        nums[i], nums[j] = nums[j], nums[i]
        
        nums[i+1:] = nums[n:i:-1]


s = Solution()
s.nextPermutation([1,3,2])

