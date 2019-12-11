class Solution:
    def sortColors(self, nums):
        n = len(nums)
        if n == 0: return
        zero = one = two = -1
        for i in range(n):
            if nums[i] == 0:
                two += 1
                nums[two] = 2
                one += 1
                nums[one] = 1
                zero += 1
                nums[zero] = 0
            elif nums[i] == 1:
                two += 1
                nums[two] = 2
                one += 1
                nums[one] = 1
            else:
                two += 1
                nums[two] = 2

s = Solution()
print(s.sortColors([2,1,2,1,1,0]))