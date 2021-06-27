class Solution:
    def unhappyFriends(self, n, preferences, pairs):
        couple = {}
        for [x, y] in pairs:
            couple[x] = y
            couple[y] = x
        ans = 0
        for x in range(n):
           for maybe in preferences[x][0:preferences[x].index(couple[x])]:
               if preferences[maybe].index(x) < preferences[maybe].index(couple[maybe]):
                   ans += 1
                   break
        return ans

a = Solution()
print(a.unhappyFriends(n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]))