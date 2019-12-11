class Solution:
    def getPermutation(self, n, k):
        p = [1]
        for i in range(1, n+1):
            p.append(p[i-1]*i)
        digit = list("123456789")
        num = n-1
        res = ""
        while num:
            t = (k-1)//p[num]
            k = k - t*p[num]
            res += digit[t]
            digit.remove(digit[t])
            num -= 1
        res += digit[k-1]
        return res

s = Solution()
print(s.getPermutation(3,3))
