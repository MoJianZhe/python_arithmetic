# 21.移除元素
from typing import List


def removeElement(nums: List[int], val: int) -> int:
    low, fast = 0, 0
    while fast < len(nums):
        if nums[fast] != val:
            nums[low] = nums[fast]
            low = low + 1
        fast += 1
    return low


#  283. 异动0
def moveZeroes(nums: List[int]) -> None:
    p = removeElement(nums, 0)
    while p < len(nums):
        nums[p] = 0
        p += 1
