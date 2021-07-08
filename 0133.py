import copy
class Solution:
    def cloneGraph(self, node):
        return copy.deepcopy(node)