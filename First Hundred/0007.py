class Solution:
    def reverse(self, x):
        max_int = 0x7FFFFFFF
        min_int = -max_int-1
        s = str(x)
        if s[0] == '-':
            return int(s[0]+str(int(s[1:][::-1]))) if int(s[0]+str(int(s[1:][::-1]))) > min_int else 0
        else:
            return int(str(int(s[::-1]))) if int(str(int(s[::-1]))) < max_int else 0

s = Solution()
print(s.reverse(120))