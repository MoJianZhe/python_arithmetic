# 给数组和 i,j , 计算[i,j] 累计值
# 存 pre[i] sum[i,j]=pre[j]-pre[i-1]
from typing import List


class NumArray:
    pre = []

    def __init__(self, nums: List[int]):
        pre = [None] * (len(nums) + 1)
        pre[0] = nums[0]
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] + nums[i]

    # 查询闭区间 [left, right] 的累加和
    def sumRange(self, left: int, right: int) -> int:
        index = left - 1 if left > 0 else left
        return self.pre[right] - self.pre[index]


## 存储百度的统计数据就用的这种方法，每次存的是总值。


# solution by labula
class NumArray:
    # 前缀和数组
    def __init__(self, nums: List[int]):
        # 输入一个数组，构造前缀和
        # preSum[0] = 0，便于计算累加和
        self.preSum = [0] * (len(nums) + 1)
        # 计算 nums 的累加和
        for i in range(1, len(self.preSum)):
            self.preSum[i] = self.preSum[i - 1] + nums[i - 1]

    # 查询闭区间 [left, right] 的累加和
    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right + 1] - self.preSum[left]
