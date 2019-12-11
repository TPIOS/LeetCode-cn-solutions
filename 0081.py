class Solution:
    def search(self, nums, target):
        try:
            nums.index(target)
            return True
        except:
            return False

s = Solution()
print(s.search([2,5,6,0,0,1,2],0))