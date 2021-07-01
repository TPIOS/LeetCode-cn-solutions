class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.ans = 1
    def dfsMain(self, node, maxValue):
        if node == None: return
        if maxValue <= node.val:
            self.ans += 1
        maxValue = max(maxValue, node.val)
        self.dfsMain(node.left, maxValue)
        self.dfsMain(node.right, maxValue)
    def goodNodes(self, root):
        self.dfsMain(root.left, root.val)
        self.dfsMain(root.right, root.val)
        return self.ans