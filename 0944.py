class Solution:
    def minDeletionSize(self, strs):
        ans = 0
        strLength = len(strs[0])
        n = len(strs)
        for i in range(strLength):
            for j in range(0, n-1):
                if strs[j][i] > strs[j+1][i]:
                    ans += 1
                    break
        return ans

a = Solution()
print(a.minDeletionSize(strs = ["zyx","wvu","tsr"]))