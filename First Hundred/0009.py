class Solution:
    def isPalindrome(self, x):
        if x < 0: return False
        s = str(x)
        return True if s == s[::-1] else False

s = Solution()
print(s.isPalindrome(10))