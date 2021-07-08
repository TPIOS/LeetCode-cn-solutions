import copy
class Solution:
    def haveNotSet(self, strs, lastcheck = -1):
        n = len(strs)
        if lastcheck == -1:
            for i in range(0, n-1):
                if strs[i+1] < strs[i]:
                    return True
            return False
        else:
            for i in range(n):
                strs[i] = strs[i][:lastcheck+1]
            for i in range(0, n-1):
                if strs[i+1] < strs[i]:
                    return True
            return False
    def minDeletionSize(self, strs):
        ans = 0
        n = len(strs)
        lastCheck = 0
        strLength = len(strs[0])
        tempStr = copy.deepcopy(strs)
        while self.haveNotSet(tempStr):
            flag = False
            for i in range(strLength):
                if self.haveNotSet(copy.deepcopy(tempStr), i):
                    ans += 1
                    flag = True
                    lastCheck = i
                    # print(lastCheck, tempStr[0])
                    break
            if flag:
                for i in range(n):
                    tempStr[i] = tempStr[i][:lastCheck] + tempStr[i][lastCheck+1:]
            strLength = len(tempStr[0])
        # print(tempStr[0])
        return ans

a = Solution()
# print(a.minDeletionSize(["zyx","wvu","tsr"]))
print(a.minDeletionSize(strs=['avv','avd','bcd']))