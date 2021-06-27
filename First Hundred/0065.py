class Solution:
    def isNumber(self, s):
        try:
            float(s)
            return True
        except:
            return False

s = Solution()
print(s.isNumber("2,000"))