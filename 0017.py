class Solution:
    def __init__(self):
        self.d = {
                    2:['a','b','c'],
                    3:['d','e','f'],
                    4:['g','h','i'],
                    5:['j','k','l'],
                    6:['m','n','o'],
                    7:['p','q','r','s'],
                    8:['t','u','v'],
                    9:['w','x','y','z']
                 }
        
        self.res = []

    def make(self, nums, tmp):
        if len(nums) == 0:
            self.res.append(tmp)
            return
        
        for s in self.d[int(nums[0])]:
            self.make(nums[1:],tmp+s)

    def letterCombinations(self, digits):
        if digits == "": return []
        self.make(digits,"")
        return self.res

s = Solution()
print(s.letterCombinations("23"))