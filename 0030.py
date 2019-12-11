class Solution:
    def __init__(self):
        self.wordsList = {}

    def search(self, s, start, end, l):
        tmp = self.wordsList.copy()
        for i in range(start, end, l):
            local = s[i:i+l]
            if tmp.get(local):
                if tmp[local] > 1:
                    tmp[local] -= 1
                else:
                    del(tmp[local])
                    if len(tmp) == 0:
                        return True
            else:
                return False

    def findSubstring(self, s, words):
        if len(s) == 0 or len(words) == 0: return []
        l = len(words[0])
        cnt = len(words)
        res = []

        for word in words:
            if self.wordsList.get(word):
                self.wordsList[word] += 1
            else:
                self.wordsList[word] = 1

        if len(self.wordsList) == 1 and self.wordsList.get('a'):
            for i in range(0, len(s)-cnt+1):
                res.append(i)
            return res

        for i in range(0, len(s)):
            if self.search(s, i, i+cnt*l, l):
                res.append(i)
        
        return res

s = Solution()
print(s.findSubstring("aaa",['aa','aa']))
