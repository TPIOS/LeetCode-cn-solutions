import sys
sys.setrecursionlimit(3000)

class Solution:
    def isScramble(self, s1, s2):
        if s1 == s2: return True
        if sorted(s1) != sorted(s2): return False

        for i in range(1,len(s1)):
            res = self.isScramble(s1[0:i],s2[0:i]) and self.isScramble(s1[i:],s2[i:])
            res = res or (self.isScramble(s1[0:i], s2[len(s2)-i:]) and self.isScramble(s1[i:],s2[0:len(s2)-i]))
            if res: return True
        
        return False

s = Solution()
print(s.isScramble(s1 = "great", s2 = "rgeat"))