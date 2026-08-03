# 1094.拼车
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_to = 0
        for list in trips:
            max_to = max(max_to, list[2])
        # 构建查分数组，原数组表示每个位置的人数
        self.build_diff(max_to)
        for list in trips:
            if not self.add_trip(trip=list, capacity=capacity):
                return False
        return True

    def add_trip(self, trip: List[int], capacity: int) -> bool:
        # trip[1],起始位置，trip[2] 结束位置
        start_index = trip[1]
        end_index = trip[2]
        end_index = (
            end_index - 1
        )  # 比如[2,1,5]，在第5站就下车了，所以第4站还是坐了人的。
        # trip[0]  人数
        number = trip[0]
        self.diff_index[start_index] = self.diff_index[start_index] + number
        if end_index + 1 < len(self.diff_index):
            self.diff_index[end_index + 1] = self.diff_index[end_index + 1] - number
        # 最后一个和最后一个建议都+了number , 所以如果是最后一个，差值也不会变。
        # else:
        #     self.diff_index[end_index] = self.diff_index[end_index] + number
        return self.is_ok(capacity)

    def is_ok(self, capacity) -> bool:
        a = True
        number_i = 0
        for i in range(len(self.diff_index)):
            if i == 0:
                number_i = self.diff_index[0]
                a = a and (number_i <= capacity)
            else:
                number_i = number_i + self.diff_index[i]
                a = a and (number_i <= capacity)
        return a

    def build_diff(self, max_to: int):
        # 查分数组，表示位置，index 的人数差
        self.diff_index = [0] * (max_to + 1)
        for i in range(1, max_to):
            self.diff_index[i] = self.diff_index[i] - self.diff_index[i - 1]


# solution by labuda 
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 最多有 1000 个车站
        nums = [0] * 1001
        # 构造差分解法
        df = self.Difference(nums)

        for trip in trips:
            # 乘客数量
            val = trip[0]
            # 第 trip[1] 站乘客上车
            i = trip[1]
            # 第 trip[2] 站乘客已经下车，
            # 即乘客在车上的区间是 [trip[1], trip[2] - 1]
            j = trip[2] - 1
            # 进行区间操作
            df.increment(i, j, val)

        res = df.result()

        # 客车自始至终都不应该超载
        for i in range(len(res)):
            if capacity < res[i]:
                return False
        return True

    # 差分数组工具类
    class Difference:
        # 差分数组
        def __init__(self, nums: List[int]):
            # 输入一个初始数组，区间操作将在这个数组上进行
            # 根据初始数组构造差分数组
            self.diff = [nums[0]] + [nums[i] - nums[i - 1] for i in range(1, len(nums))]

        # 给闭区间 [i, j] 增加 val（可以是负数）
        def increment(self, i: int, j: int, val: int) -> None:
            self.diff[i] += val
            if j + 1 < len(self.diff):
                self.diff[j + 1] -= val

        # 返回结果数组
        def result(self) -> List[int]:
            res = [self.diff[0]]
            # 根据差分数组构造结果数组
            for i in range(1, len(self.diff)):
                res.append(res[i - 1] + self.diff[i])
            return res
