# 1004.最大连续1的个数
from typing import List


def longestOnes(self, nums: List[int], k: int) -> int:
    # 0的数目小于k时，扩大，大于等于k，缩小
    left, right = 0, 0
    # 保存0的数目
    zero_windows = 0
    max_value = 0
    while right < len(nums):
        a = nums[right]
        if a == 0:
            zero_windows += 1
        else:
            # 如果是left移动之后，在移动right的场景，窗口移动之后，不能直接在结果上+1，因为窗口内的数据已经变了
            max_value = max_value + 1
        right += 1
        while left < right and zero_windows >= k:
            if zero_windows == k:
                max_value = max(max_value, right - left)
            b = nums[left]
            if b == 0:
                zero_windows -= 1
            left += 1
    return max_value


def longestOnes2(self, nums: List[int], k: int) -> int:
    # 0的数目小于k时，扩大，大于等于k，缩小
    left, right = 0, 0
    # 保存0的数目
    zero_windows = 0
    max_value = 0
    while right < len(nums):
        a = nums[right]
        if a == 0:
            zero_windows += 1
        right += 1
        if zero_windows < k:
            max_value = max(max_value, right - left)
        while left < right and zero_windows >= k:
            # 边界有问题，zero_windows 等于k 的时候，不需要缩小，是合法的。有可能左边是有多个1，中间是0，然后你就把它们缩小了。
            if zero_windows == k:
                max_value = max(max_value, right - left)
            b = nums[left]
            if b == 0:
                zero_windows -= 1
            left += 1
    return max_value


def longestOnes3(self, nums: List[int], k: int) -> int:
    # 0的数目小于k时，扩大，大于k，缩小
    left, right = 0, 0
    # 保存0的数目
    zero_windows = 0
    max_value = 0
    while right < len(nums):
        a = nums[right]
        if a == 0:
            zero_windows += 1
        right += 1
        if zero_windows <= k:
            max_value = max(max_value, right - left)
        while left < right and zero_windows > k:
            b = nums[left]
            if b == 0:
                zero_windows -= 1
            left += 1
    return max_value


# soluiton by labuladong
def longestOnes(self, nums: List[int], k: int) -> int:
    left, right = 0, 0
    # 记录窗口中 1 的出现次数
    windowOneCount = 0
    # 记录结果长度
    res = 0

    # 开始滑动窗口模板
    while right < len(nums):
        # 扩大窗口
        if nums[right] == 1:
            windowOneCount += 1
        right += 1

        while right - left - windowOneCount > k:
            # 当窗口中需要替换的 0 的数量大于 k，缩小窗口
            if nums[left] == 1:
                windowOneCount -= 1
            left += 1
        # 此时一定是一个合法的窗口，求最大窗口长度
        res = max(res, right - left)
    return res


if __name__ == "__main__":
    a = longestOnes2(None, [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3)
    print(a)
