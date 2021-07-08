class Solution:
    def totalFruit(self, fruits):
        n = len(fruits)
        maxFruit = -1
        start = 0
        firstKindnum, secondKindnum = 0, 0
        tempSecondKind = None
        firstKind, secondKind = None, None
        i = 0
        while i < n:
            if firstKind == None:
                firstKind = fruits[i]
                firstKindnum = 1
            elif firstKind == fruits[i]:
                firstKindnum += 1
            elif secondKind == None:
                secondKind = fruits[i]
                start = i
                secondKindnum = 1
            elif secondKind == fruits[i]:
                secondKindnum += 1
            else:
                maxFruit = max(maxFruit, firstKindnum + secondKindnum)
                i = start
                firstKind = secondKind
                firstKindnum = 1
                secondKind = None
                secondKindnum = 0
            i += 1

        maxFruit = max(maxFruit, firstKindnum + secondKindnum)
        return maxFruit

a = Solution()
print(a.totalFruit([1,2,3,2,2]))
