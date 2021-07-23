class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        for i in range(1, len(citations)+1):
            if i > citations[i-1]: return i-1
        return len(citations)