class Solution:
    def intToRoman(self, num):
        d = {
                1:'I',
                4:'IV',
                5:'V',
                9:'IX',
                10:'X',
                40:'XL',
                50:'L',
                90:'XC',
                100:'C',
                400:'CD',
                500:'D',
                900:'CM',
                1000:'M'
            }
        l = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        tmp_num = num
        idx = len(l)-1
        res = ""
        while tmp_num > 0:
            while tmp_num // l[idx] == 0: 
                idx -= 1
            md = tmp_num // l[idx]
            res += d[l[idx]] * md
            tmp_num %= l[idx]
        
        return res

s = Solution()
print(s.intToRoman(1994))
