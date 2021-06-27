import collections
class Solution:
    def minimumIncompatibility(self, nums, k):
        n=len(nums)
        # 如果n和k相等，每个子集的不兼容性为0
        if n==k:
            return 0
        # 每个子集的大小
        size = n//k
        # value记录每个合格子集的不兼容性
        value=collections.defaultdict()
        for i in range(1<<n):
            # visited记录已遍历过的数，判断是否含有重复值
            visited=set()
            # 标记子集是否合法
            flag=True
            # 子集中最大最小值
            max_,min_=float('-inf'),float('inf')
            # 判断sub中1的个数是否为size
            if bin(i).count("1")==size:
                # 判断是否含有相同元素
                for j in range(n):
                    if (i>>j) & 1:
                        if nums[j] in visited:
                            flag=False
                            break
                        max_=max(max_,nums[j])
                        min_=min(min_,nums[j])
                        visited.add(nums[j])
                # 计算不兼容性
                if flag:
                    value[i]=max_-min_
        
        # 状态压缩dp
        dp=[float('inf')]*(1<<n)
        dp[0]=0
        for i in range(1<<n):
            if bin(i).count("1")%size==0:
                # 枚举子集
                j=i
                while j:
                    if j in value:
                        # 更新状态
                        dp[i]=min(dp[i],dp[i^j]+value[j])
                    j=(j-1)&i
        return dp[-1] if dp[-1]!=float('inf') else -1

a = Solution()
print(a.minimumIncompatibility([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 8))