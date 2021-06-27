class Solution:
    def __init__(self):
        self.oneNum = [0]
        for i in range(1, 65536):
            if i % 2 == 0:
                self.oneNum.append(self.oneNum[i//2])
            else:
                self.oneNum.append(self.oneNum[i - 1] + 1)
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        m = 1 << n
        # print(n, m)
        cnt = n // k
        dp = [-1 for i in range(m)]
        value = [-1 for i in range(m)]
        for i in range(0, m):
            if self.oneNum[i] == cnt:
                flag = [0 for i in range(20)]
                for j in range(0, n):
                    if i & (1 << j):
                        flag[nums[j]] += 1       
                if max(flag) <= 1:
                    minNum = 1e9
                    maxNum = -1e9
                    for j in range(1, n+1):
                        if flag[j]:
                            minNum = min(minNum, j)
                            maxNum = max(maxNum, j)
                    value[i] = maxNum - minNum
        dp[0] = 0
        for i in range(0, m):
            if self.oneNum[i] % cnt == 0:
                j = i
                while j != 0:
                    if value[j] != -1 and dp[i^j] != -1:
                        if dp[i] == -1:
                            dp[i] = dp[i^j]+value[j]
                        else:
                            dp[i] = min(dp[i], dp[i^j]+value[j])
                    j = (j-1)&i
        return dp[m-1]

a = Solution()
print(a.minimumIncompatibility([1,2,1,4], 2))