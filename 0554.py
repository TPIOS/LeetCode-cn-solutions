class Solution:
    def leastBricks(self, wall):
        cnt = {0: 0}
        for block in wall:
            pos = 0
            # print(block[:-1])
            for brick in block[:-1]:
                pos += brick
                if pos not in cnt:
                    cnt[pos] = 1
                else:
                    cnt[pos] += 1
        return len(wall)-max(cnt.values())

a = Solution()
print(a.leastBricks(wall=[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))