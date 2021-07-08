class Solution:
    def btreeGameWinningMove(self, root, n, x):
        self.x_left, self.y_left = 0, 0
        def count_nodes(node):
            if node is None:
                return 0
            left = count_nodes(node.left)
            right = count_nodes(node.right)
            if node.val == x:
                self.x_left, self.x_right = left, right
            return 1 + left + right
            
        count_nodes(root)
        parent = n - self.x_left - self.x_right - 1
        select = max([self.x_left, self.x_right, parent])
        if select > n - select:
            return True
        return False