class Solution:
    def addBinary(self, a, b):
        a = int(a, base=2)
        b = int(b, base=2)
        res = bin(a+b)[2:]
        return res

s = Solution()
print(s.addBinary('11','1'))