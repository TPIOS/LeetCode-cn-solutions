import itertools
class Solution:
    def combine(self, n, k):
        res = []
        for i in range(n): res.append(i+1)
        return list(itertools.combinations(res,k))

s = Solution()
print(s.combine(3,2))