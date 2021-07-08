class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        rpl = [(i, s, t) for i, s, t in zip(indexes, sources, targets)]
        rpl = sorted(rpl, key=lambda x: x[0], reverse=True)
        res = list(S)
        for i, s, t in rpl:
            if S[i: i+len(s)] == s:
                for j in range(i, i+len(s)):
                    res[j] = ""
                res[j] = t

        return "".join(res)