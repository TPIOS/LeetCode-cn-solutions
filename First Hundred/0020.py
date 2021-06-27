class Solution:
    def isValid(self, s):
        l = list()
        left = ['(','[','{']
        right = [')',']','}']
        for c in s:
            if c in left:
                l.append(c)
            elif c in right:
                if len(l) == 0:
                    return False
                if right.index(c) == left.index(l[-1]):
                    l.pop()
                else:
                    return False
        
        if len(l) == 0:
            return True
        else:
            return False

s = Solution()
print(s.isValid('{[]}'))
