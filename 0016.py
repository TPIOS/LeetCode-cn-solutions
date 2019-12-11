class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        l = nums.__len__()
        min_sum = nums[0]+nums[1]+nums[2]
        for k in range(l):
            # if nums[k] > target-min_sum: break
            if k > 0 and nums[k] == nums[k-1]: continue
            i = k + 1
            j = l - 1
            while i < j:
                if abs(target - (nums[i]+nums[j]+nums[k])) < abs(target - min_sum):
                    min_sum = nums[i]+nums[j]+nums[k]
                if nums[i] + nums[j] == target-nums[k]:
                    return target
                elif nums[i] + nums[j] < target-nums[k]:
                    i += 1
                else:
                    j -= 1
                
                # while i<j and nums[i] == nums[i+1]: i += 1
                # while i<j and nums[j] == nums[j-1]: j -= 1        

        return min_sum

s = Solution()
print(s.threeSumClosest([1,2,4,8,16,32,64,128],82))
