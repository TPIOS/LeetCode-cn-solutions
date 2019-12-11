class Solution:
    def grayCode(self, n):
        res = [0]
        cnt = 0
        while cnt <= n-1:
            cnt += 1
            m = len(res)
            transfer = 1 << cnt - 1
            for i in range(m-1, -1, -1):
                res.append(res[i]|transfer)
        return res

s = Solution()
print(s.grayCode(3))
            