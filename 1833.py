class Solution:
    def maxIceCream(self, costs, coins):
        costs.sort()
        ans = 0
        for iceCream in costs:
            if coins - iceCream >= 0:
                ans += 1
                coins -= iceCream
        return ans

a = Solution()
print(a.maxIceCream())