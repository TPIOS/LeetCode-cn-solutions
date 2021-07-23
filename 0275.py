class Solution:
    def hIndex(self, citations):
        n = len(citations)
        l, r = 0, n
        while l < r:
            mid = l + (r - l) // 2
            if citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid
        return n - l