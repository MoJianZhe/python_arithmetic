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
    # 此解法没考虑到 head 一直重复的情况，例如:[1,1,1,2,3] 它会返回 [1,2,3],预期 [2,3]
###################################################################################################################

def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
    p1 = head
    # p2 晚 p1 一步
    p2 = ListNode(None)
    p2.next = head 
    while p1 and p1.next:
        if p1.val != p1.next.val:
            p1 = p1.next
            p2 = p2.next
            continue
        # 重复数据集合为：[rm,p1) ，这样，p1 才可以继续往下走
        rm = p1
        p1 = p1.next
        while p1 is not None and rm.val == p1.val:
            p1 = p1.next
        p2.next = p1
        # 初始值重复的场景
        if head == rm :
            head = p1
        rm = None
    return head
   

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/solutions/2004067/ru-he-qu-zhong-yi-ge-shi-pin-jiang-tou-p-2ddn/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
def deleteDuplicatesOther(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cur = dummy = ListNode(next=head)
    while cur.next and cur.next.next:
        val = cur.next.val
        if cur.next.next.val == val:  # 后两个节点值相同
            # 值等于 val 的节点全部删除
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next

