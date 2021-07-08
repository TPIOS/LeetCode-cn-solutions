class Solution:
    def location(self, s):
        sub = ord(s) - 65
        return sub//6, sub%6

    def distance(self, c1, c2):
        c1x, c1y = self.location(c1)
        c2x, c2y = self.location(c2)
        return abs(c1x-c2x)+abs(c1y-c2y)

    def minimumDistance(self, word):
        leftHand = word[0]
        rightHand = {chr(i): 0 for i in range(65, 65+26)}
        for c in word[1:]:
            d = self.distance(leftHand, c)
            nR = {chr(i): rightHand[chr(i)]+d for i in range(65, 65+26)}
            nR[leftHand] = min(nR[leftHand], min(self.distance(r, c) + rightHand[r] for r in rightHand))
            leftHand, rightHand = c, nR
        
        return min(rightHand.values())