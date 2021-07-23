import bisect
class Solution:
    def minAbsoluteSumDiff(self, nums1, nums2):
        MOD = 10**9 + 7
        s1_sorted = sorted(nums1)
        n = len(nums1)
        res = 0
        optimal = float('inf')
        for idx, value in enumerate(nums2):
            diff = abs(nums1[idx] - nums2[idx])
            res += diff
            j = bisect.bisect_left(s1_sorted, value)
            if optimal <= -diff:
                continue
            if j:
                optimal = min(optimal, abs(s1_sorted[j-1] - value) - diff)
            if j < n:
                optimal = min(optimal, abs(s1_sorted[j] - value) - diff)
        
        return (res + optimal) % MOD
