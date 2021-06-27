import itertools
class Solution:
    def permute(self, nums):
        tmp_res = list(set(list(itertools.permutations(nums,len(nums)))))
        res = []
        for one in tmp_res: res.append(list(one))
        return res

s = Solution()
print(s.permute([1,1,3]))