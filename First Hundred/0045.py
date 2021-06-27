class Solution:
    def jump(self, nums):
        n = len(nums)
        if n == 0 or n == 1: return 0
        idx = pos =0
        cnt = 0
        while True:
            new_pos = pos
            while idx <= pos:
                new_pos = max(new_pos, idx + nums[idx])
                idx += 1
            
            cnt += 1
            pos = new_pos
            if pos >= n-1: break
        
        return cnt
