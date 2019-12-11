# class Solution:
#     def check(self, height, k):
#         if k == 0 or max(height[0:k]) <= height[k]: return False
#         if k == len(height) - 1 or max(height[k:]) <= height[k]: return False
#         return True

#     def trap(self, height):
#         tot = 0
#         n = len(height)
#         if n == 0 or n == 1: return 0
#         h = max(height)

#         for i in range(0,h):
#             for k in range(0,n):
#                 if height[k] == i and self.check(height, k):
#                     height[k] += 1
#                     tot += 1

#         return tot

class Solution:
    def trap(self, height):
        n = len(height)
        if n <= 2: return 0
        left = [-1] * n
        right = [-1] * n
        
        max_idx = 0
        max_height = height[0]
        left[0] = 0
        for i in range(1, n):
            if height[i] >= max_height:
                max_idx = i
                max_height = height[i]
            left[i] = max_idx
        
        right[n-1] = n - 1
        max_idx = n - 1
        max_height = height[n-1]
        for i in range(n-2, -1, -1):
            if height[i] >= max_height:
                max_idx = i
                max_height = height[i]
            right[i] = max_idx
        
        tot = 0
        for i in range(0, n):
            tot += min(height[left[i]], height[right[i]]) - height[i]

        return tot

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))