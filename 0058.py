class Solution:
    def lengthOfLastWord(self, s):
        res = s.split()
        if len(res) != 0 and res[-1].isalpha():
            return len(res[-1])
        else:
            return 0

s = Solution()
print(s.lengthOfLastWord("Hello World"))
        