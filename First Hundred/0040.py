class Solution:
    def __init__(self):
        self.res = {}
    
    def search(self, candidates, target, tmp):
        if target < 0: return

        if target == 0:
            self.res[" ".join(tmp.copy())] = 1
            return

        for i in range(len(candidates)):
            tmp.append(str(candidates[i]))
            self.search(candidates[i+1:], target-candidates[i], tmp)
            tmp.pop()

    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.search(candidates, target, [])
        res = []
        for key, value in self.res.items():
            tmp = key.split(' ')
            nums = []
            for num in tmp:
                nums.append(int(num))
            res.append(nums)
        
        return res
    
s = Solution()
print(s.combinationSum2(candidates = [2,5,2,1,2], target = 5))
