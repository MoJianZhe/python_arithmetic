# 75.颜色分类
from typing import List


def sortColors(self, nums: List[int]) -> None:
    # [0,p0) 保存0，(p2,len-1] 保持2
    p0=0
    p = 0
    p2 = len(nums)-1
    while p<=p2:
        if nums[p]==0:
            nums[p0],nums[p]=nums[p],nums[p0]
            p0 = p0+1
        if nums[p] ==2:
            nums[p],nums[p2]=nums[p2],nums[p]
            p2 = p2 -1
        if nums[p] ==1:
            p= p+1
        if p<p0:
            p=p0
    