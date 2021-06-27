import collections
class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        m = 1 << n
        if n == k: return 0
        cnt = n // k
        dp = [float('inf')] * m
        value = collections.defaultdict()
        for i in range(0, m):
            visited = set()
            flag = True
            minNum, maxNum = 1e10, -1e10
            if bin(i).count("1") == cnt:
                for j in range(0, n):
                    if (i>>j) & 1:
                        if nums[j] in visited:
                            flag=False
                            break
                        maxNum = max(maxNum, nums[j])
                        minNum = min(minNum, nums[j])
                        visited.add(nums[j])
                if flag:
                    value[i] = maxNum - minNum

        dp[0] = 0
        for i in range(0, m):
            if bin(i).count("1") % cnt == 0:
                j = i
                while j:
                    if j in value:
                        dp[i] = min(dp[i], dp[i^j]+value[j])       
                    j = (j-1)&i
        return dp[-1] if dp[-1]!=float('inf') else -1

a = Solution()
print(a.minimumIncompatibility([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 8))