# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, left, right, res):
        if left > right: res.append(None); return
        left_res = list()
        right_res = list()
        for i in range(left, right+1):
            self.dfs(left, i-1, left_res)
            self.dfs(i+1, right, right_res)
            l = len(left_res)
            r = len(right_res)
            for j in range(l):
                for k in range(r):
                    root = TreeNode(i)
                    root.left = left_res[j]
                    root.right = right_res[k]
                    res.append(root)
            left_res = list()
            right_res = list()
            
    def generateTrees(self, n):
        res = []
        if n <= 0: return res
        self.dfs(1,n,res)
        return res
        