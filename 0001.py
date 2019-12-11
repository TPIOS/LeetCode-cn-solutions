def twosum(nums, target):
    d = dict()
    idx = 0
    for num in nums:
        d[str(num)] = idx
        idx += 1
    
    idx = 0
    for num in nums:
        idx_2 = d.get(str(target-num))
        if idx_2:
            return [idx, idx_2]
        idx += 1

res = twosum([2,7,11,15],9)
print(res)
