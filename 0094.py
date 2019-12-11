# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        res = []
        stack = []
        if root == None: return res
        p = root
        while True:
            while p != None:
                stack.append(p)
                p = p.left
            if len(stack) == 0: break
            p = stack.pop()
            res.append(p.val)

            p = p.right
        
        return res

        
        