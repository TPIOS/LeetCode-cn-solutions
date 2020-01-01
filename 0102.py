# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ansList = list()
        if not root: return []
        def BFS(node, level):
            if len(ansList) == level:
                ansList.append([])
            ansList[level].append(node.val)
            if node.left:
                BFS(node.left, level+1)
            if node.right:
                BFS(node.right, level+1)
        BFS(root, 0)
        return ansList
