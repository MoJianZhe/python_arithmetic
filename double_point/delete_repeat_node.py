# 82.删除排序列表的重复数
from typing import Optional

from link.list_node import ListNode


def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    p1 = head.next
    p2 = head
    while p1 and p1.next:
        if p1.val != p1.next.val:
            p1 = p1.next
            p2 = p2.next
            continue
        # rm = p1
        # while rm ==p1.next:
        #     p1 = p1.next  这样 p1 就属于重复数据，p1没法往下走。先要定义好rm 和 p1 的边界
        # 删掉循环的数据
        # p2.next = p1.next

        # 重复数据集合为：[rm,p1) ，这样，p1 才可以继续往下走
        rm = p1
        p1 = p1.next
        while rm.val == p1.val:
            # a = p1
            # a.next = None
            p1 = p1.next
        p2.next = p1
        rm = None
    return head
    # 此解法没考虑到 head 一直重复的情况，例如:[1,1,1,2,3] 它会返回 [1,2,3],逾期 [2,3]
###################################################################################################################

def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    p1 = head.next
    p2 = head
    while p1 and p1.next:
        if p1.val != p1.next.val:
            p1 = p1.next
            p2 = p2.next
            continue

        # 重复数据集合为：[rm,p1) ，这样，p1 才可以继续往下走
        rm = p1
        p1 = p1.next
        while rm.val == p1.val:
            p1 = p1.next
        p2.next = p1
        rm = None
    return head
    # 此解法没考虑到 head 一直重复的情况，例如:[1,1,1,2,3] 它会返回 [1,2,3],逾期 [2,3]
