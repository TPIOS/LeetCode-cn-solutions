# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.error1 = None
        self.error2 = None
        self.tmp = None
    def dfs(self, root):
        if root == None: return
        if root.left != None: self.dfs(root.left)
        
        if self.tmp != None and self.tmp.val > root.val:
            if self.error1 == None:
                self.error1 = self.tmp
                self.error2 = root
            else:
                self.error2 = root
        
        self.tmp = root

        if root.right != None: self.dfs(root.right)

    def recoverTree(self, root):
        self.dfs(root)
        if self.error1 != None and self.error2 != None:
            self.error1.val, self.error2.val = self.error2.val, self.error1.val