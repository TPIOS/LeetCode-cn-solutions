import math
class Solution:
    def numTrees(self, n):
        return int(math.factorial(2*n)//(math.factorial(n)**2))//(n+1)