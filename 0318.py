class Solution:
    def maxProduct(self, words):
        maxRes = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1, n):
                newStr = words[i] + words[j]
                if len(set(list(newStr))) == len(set(list(words[i]))) + len(set(list(words[j]))):
                    maxRes = max(maxRes, len(words[i]) * len(words[j]))
        return maxRes

a = Solution()
print(a.maxProduct(["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]))