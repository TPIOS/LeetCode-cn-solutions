class Solution:
    def groupAnagrams(self, strs):
        d = dict()
        for s in strs:
            tmp = "".join(sorted(list(s)))
            if tmp in d:
                d[tmp].append(s)
            else:
                d[tmp] = [s]
        return list(d.values())

s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))