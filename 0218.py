import heapq
class Solution:
    def getSkyline(self, buildings):
        infoLine = []
        n = len(buildings)
        for i in range(n):
            left, right, height = buildings[i]
            infoLine.append([left, height, right])
            infoLine.append([right, 0, float('inf')])
        infoLine.sort(key = lambda x: (x[0], -x[1]))
        queue = [[-infoLine[0][1], infoLine[0][2]]]
        res = [[infoLine[0][0], infoLine[0][1]]]
        for i in range(1, len(infoLine)):
            start, height, end = infoLine[i]
            pre = queue[0][0]
            while queue and start >= queue[0][1]:
                heapq.heappop(queue)
            heapq.heappush(queue, [-height, end])
            if queue[0][0] != pre:
                res.append([start, -queue[0][0]])
        return res