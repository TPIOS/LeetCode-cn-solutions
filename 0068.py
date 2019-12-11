class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        tmp_wordList = [words[0]]
        cnt_len = len(words[0])

        for word in words[1:]:
            if cnt_len + len(word) + 1 <= maxWidth:
                tmp_wordList.append(word)
                cnt_len += len(word) + 1
            else:
                tot = len("".join(tmp_wordList))
                n = len(tmp_wordList)
                space_need = maxWidth - tot
                if n == 1:
                    tmp = tmp_wordList[0] + ' '*space_need
                    res.append(tmp)
                    tmp_wordList = [word]
                    cnt_len = len(word)
                    continue
                if space_need % (n-1) == 0:
                    space_num = space_need // (n-1)
                    tmp = (" "*space_num).join(tmp_wordList)
                    res.append(tmp)
                    tmp_wordList = [word]
                    cnt_len = len(word)
                else:
                    space_num = space_need // (n-1)
                    space_left = space_need - space_num*(n-1)
                    tmp = (" "*(space_num+1)).join(tmp_wordList[:space_left+1]) + " "*space_num + (" "*space_num).join(tmp_wordList[space_left+1:])
                    res.append(tmp)
                    tmp_wordList = [word]
                    cnt_len = len(word)
        
        if cnt_len > 0:
            tmp = " ".join(tmp_wordList)
            tot = len(tmp)
            space_need = maxWidth - tot
            tmp += " "*space_need
            res.append(tmp)
        
        return res

s = Solution()
print(s.fullJustify(["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"],
16))