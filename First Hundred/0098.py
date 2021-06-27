# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def check(self, root, small, large):
        if root == None: return True
        if small >= root.val or large <= root.val: return False
        return self.check(root.left, small, root.val) and self.check(root.right, root.val, large)

    def isValidBST(self, root):
        return self.check(root,-0x7fffffff-1,0x7fffffff+1)