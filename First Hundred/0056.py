import copy
# Definition for an interval.
class Section:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __lt__(self, other):
        return self.start < other.start

    def __le__(self, other):
        return self.start <= other.start

    def __eq__(self, other):
        return self.start == other.start

    def __ge__(self, other):
        return self.start >= other.start

    def __gt__(self, other):
        return self.start > other.start

    def __ne__(self, other):
        return self.start != other.start

class Solution:
    def merge(self, intervals):
        n = len(intervals)
        if n <= 1: return intervals
        transfers = []
        for interval in intervals:
            transfers.append(Section(interval.start, interval.end))
        transfers.sort()
        res = []
        new_transfer = Section(transfers[0].start, transfers[0].end)
        for i in range(1,n):
            if transfers[i].start <= new_transfer.end:
                if transfers[i].end >= new_transfer.end:
                    new_transfer.end = transfers[i].end
            else:
                res.append(copy.deepcopy(new_transfer))
                new_transfer.start = transfers[i].start
                new_transfer.end = transfers[i].end

        # print(len(res))
        if len(res) == 0 or (res[-1].start != new_transfer.start or res[-1].end != new_transfer.end):
            res.append(new_transfer)

        final_res = []
        for transfer in res:
            final_res.append(Interval(transfer.start, transfer.end))
        
        return final_res