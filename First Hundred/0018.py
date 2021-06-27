class Solution:
    def fourSum(self, nums, target):
        max_num = 0x7fffffff
        res = []
        tmp = [max_num,max_num,max_num,max_num]
        n = nums.__len__()
        d = {}
        nums.sort()
        for i1 in range(n):
            tmp[0] = nums[i1]
            for i2 in range(i1+1,n):
                tmp[1] = nums[i2]
                i3 = i2 + 1
                i4 = n - 1
                while i3 < i4:
                    total = nums[i1]+nums[i2]+nums[i3]+nums[i4]
                    if total < target:
                        i3 += 1
                    elif total > target:
                        i4 -= 1
                    else:
                        tmp[2] = nums[i3]
                        tmp[3] = nums[i4]
                        ss = str(tmp[0])
                        for k in range(1,4):
                            ss += " " + str(tmp[k])
                        if not (ss in d):
                            d[ss] = 1
                            res.append([tmp[0],tmp[1],tmp[2],tmp[3]])
                        i3 += 1
        return res

s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2],0))