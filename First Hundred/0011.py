class Solution:
    def maxArea(self, h):
        i = 0
        j = h.__len__() - 1
        res = -1
        while i < j:
            res = max((min(h[i], h[j]) * (j-i)), res)
            if h[i] < h[j]:
                i += 1
            else:
                j -= 1

        return res

a = Solution()
print(a.maxArea([1,1]))