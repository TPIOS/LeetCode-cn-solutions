class Solution:
    def numberOfSubarrays(self, nums, k):
        n = len(nums)
        cnt = 0
        oddIdx = [-1]
        for i in range(n):
            if nums[i] % 2 == 1:
                oddIdx.append(i)
                cnt += 1
        oddIdx.append(n)
        res = 0
        for i in range(1, cnt + 2 - k):
            res += (oddIdx[i] - oddIdx[i - 1]) * (oddIdx[i + k] - oddIdx[i + k - 1])
        
        return res
    
a = Solution()
print(a.numberOfSubarrays(nums = [1,1,2,1,1], k = 3))