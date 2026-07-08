# 160.相交链表
# 1、解法1，还是用hash set 保存，看是否重复
from link.list_node import ListNode
from typing import Optional


# A 遍历完了之后，再开始走B；B遍历完了开始走A。 相等的时候，说明有相交。
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    p1 = headA
    p2 = headB
    while p1 or p2:  # 应该是 or 而不是 and , 因为p1 可能先走完。
        # 下一步的时候，应该优先判断是否到达边界值。
        if p1 is None:
            p1 = headB
        if p2 is None:
            p2 = headA
        if p1 == p2:
            return p1
        # 下一步
        p1 = p1.next
        p2 = p2.next
    return None


# solution by labula
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    # p1 指向 A 链表头结点，p2 指向 B 链表头结点
    p1, p2 = headA, headB
    while p1 != p2:
        # p1 走一步，如果走到 A 链表末尾，转到 B 链表
        p1 = headB if p1 is None else p1.next
        # p2 走一步，如果走到 B 链表末尾，转到 A 链表
        p2 = headA if p2 is None else p2.next
    return p1
