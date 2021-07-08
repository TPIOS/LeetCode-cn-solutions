class Solution:
    def findKthBit(self, n, k, invert=False):
        if n == 1:
            return "0" if not invert else "1"

        length = 2 ** n - 1
        split = length // 2

        if k - 1 < split:
            return self.findKthBit(n-1, k, invert)
        elif k - 1 > split:
            return self.findKthBit(n-1, length - k + 1, not invert)
        else:
            return "1" if not invert else "0"