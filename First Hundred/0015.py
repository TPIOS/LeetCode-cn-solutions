class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        l = nums.__len__()
        for k in range(l):
            if nums[k] > 0: break # easy to think about this optimization
            if k > 0 and nums[k] == nums[k-1]: continue #cancel the repeated number
            i = k + 1
            j = l - 1
            while i < j:
                if nums[i] + nums[j] == -nums[k]:
                    res.append([nums[k],nums[i],nums[j]])
                    while i<j and nums[i] == nums[i+1]: i += 1
                    while i<j and nums[j] == nums[j-1]: j -= 1
                    i += 1
                    j -= 1 #key optimization
                    #don't break here, because one number may have many solutions
                elif nums[i] + nums[j] < -nums[k]:
                    i += 1
                else:
                    j -= 1

        return res

s = Solution()
print(s.threeSum([1,-1,-1,0]))
