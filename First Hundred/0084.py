class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        if n == 0: return 0
        left = [0]*n
        right = [0]*n
        
        left[0] = 0
        for i in range(1,n):
            left[i] = i
            j = i
            while left[j] - 1 >=0 and heights[left[j]-1] >= heights[i]:
                j = left[j] - 1
            left[i] = left[j]
        
        right[n-1] = n-1
        for i in range(n-2,-1,-1):
            right[i] = i
            j = i
            while right[j] + 1 <= n-1 and heights[right[j] + 1] >= heights[i]:
                j = right[j] + 1
            right[i] = right[j]
        
        res = -1
        for i in range(n):
            res = max(res, heights[i]*(right[i]-left[i]+1))
        
        return res