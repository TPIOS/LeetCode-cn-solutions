class Solution:
    def getStrongest(self, arr, k):
        arr.sort()
        return sorted(arr, key=lambda x: (-abs(x - arr[(len(arr) - 1) // 2]), -x))[:k]