class Solution:
    def longestBeautifulSubstring(self, word):
        res = 0
        dic = "aeiou"
        n = len(word)
        p, cnt = 0, 0
        i = 0
        while i < n:
            if word[i] != dic[p]:
                p = 0
                cnt = 0
                if dic[0] != word[i]: i += 1
            else:
                while word[i]==dic[p]:
                    cnt += 1
                    i += 1
                if dic[p] == 'u':
                    res = max(res, cnt)
                else:
                    p += 1
        return res
