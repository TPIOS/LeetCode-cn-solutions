import itertools
class Solution:
    def permuteUnique(self, nums):
        tmp_res = list(set(list(itertools.permutations(nums,len(nums)))))
        res = []
        for one in tmp_res: res.append(list(one))
        return res
