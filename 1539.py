class Solution:
    def findKthPositive(self, arr, k):
        start = 0
        n = len(arr)
        for i in range(n):
            distance = arr[i] - start - 1
            if k > distance:
                k -= distance
                start = arr[i]
            else:
                return start + k
        return start + k

a = Solution()
print(a.findKthPositive())