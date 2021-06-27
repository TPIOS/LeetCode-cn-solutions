class Solution:
    def __init__(self):
        self.res = []
    
    def search(self, candidates, target, tmp):
        if target < 0: return

        if target == 0:
            self.res.append(tmp.copy())
            return

        for i in range(len(candidates)):
            tmp.append(candidates[i])
            self.search(candidates[i:], target-candidates[i], tmp)
            tmp.pop()

    def combinationSum(self, candidates, target):
        self.search(candidates, target, [])
        return self.res
    
s = Solution()
print(s.combinationSum([2,3,6,7], 7))
        