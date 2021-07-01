class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root):
        current = root
        while current:
            if current.left:
                pred = current.left
                nxt = current.left
                while pred.right:
                    pred = pred.right
                pred.right = current.right
                current.left = None
                current.right = nxt
            current = current.right 