class Solution:
    def findFather(self, father, x):
        if father[x] == x:
            return x
        else:
            return self.findFather(father, father[x])

    def unionMain(self, father, x, y):
        rootX = self.findFather(father, x)
        rootY = self.findFather(father, y)
        father[rootY] = rootX

    def makeConnected(self, n, connections):
        if len(connections) < n-1: return -1
        father = {}
        for i in range(n): father[i] = i
        for connection in connections:
            self.unionMain(father, connection[0], connection[1])
        ans = 0
        for i in range(n):
            if father[i] == i:
                ans += 1
        return ans - 1

a = Solution()
print(a.makeConnected())