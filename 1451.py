class Solution:
    def arrangeWords(self, text):
        words = text.lower().split(" ")
        # lenDict = {}
        lenList = []
        for idx, word in enumerate(words):
            lenList.append([len(word), idx, word])
        lenList = sorted(lenList)
        res = []
        for _, __, word in lenList: res.append(word)
        res[0] = res[0].capitalize()
        return " ".join(res)


a = Solution()
print(a.arrangeWords("To be or not to be"))