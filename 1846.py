class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        n = len(arr)
        arr.sort()
        start = arr[0]
        if start != 1:
            start = 1
            arr[0] = 1
        for idx in range(1,n):
            if arr[idx] - start > 1:
                start = start + 1
                arr[idx] = start
            else:
                start = arr[idx]
        return arr[-1]

a = Solution()
print(a.maximumElementAfterDecrementingAndRearranging([2,2,1,2,1]))