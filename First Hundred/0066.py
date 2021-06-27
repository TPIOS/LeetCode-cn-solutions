class Solution:
    def plusOne(self, digits):
        n = len(digits)
        digits[-1] += 1
        for i in range(n-1,0,-1):
            if digits[i] == 10:
                digits[i] = 0
                digits[i-1] += 1
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0,1)
        return digits

s = Solution()
print(s.plusOne([9,9]))