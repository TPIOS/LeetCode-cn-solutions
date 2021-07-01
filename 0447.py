class Solution:
    def numberOfBoomerangs(self, points):
        ans = 0
        for point1 in points:
            d = {}
            for point2 in points:
                distance = (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2
                if distance not in d:
                    d[distance] = 1
                else:
                    d[distance] += 1
            for val in d.values():
                if val >= 2:
                    ans += val*(val-1)
        return ans