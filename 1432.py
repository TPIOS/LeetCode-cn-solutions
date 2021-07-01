class Solution:
    def maxDiff(self, num):
        max_num = str(num)
        for digit in max_num:
            if digit != '9':
                max_num = max_num.replace(digit, '9')
                break
        
        min_num = str(num)
        highest = min_num[0]
        if highest == '1':
            for digit in min_num:
                if digit != '0' and digit != '1':
                    min_num = min_num.replace(digit, '0')
                    break
        else:
            min_num = min_num.replace(highest, '1')
        return int(max_num) - int(min_num)

a = Solution()
print(a.maxDiff(123456))
