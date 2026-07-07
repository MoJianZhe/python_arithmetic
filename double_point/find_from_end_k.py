# 寻找倒数第k个节点（链表数据结构）
# 要求一次遍历
from link.list_node import ListNode


def findFromEnd(head: ListNode, k: int) -> ListNode:
    p1 = head
    for i in range(k):
        p1 = p1.next
    p2 = head
    while p1 is not None:
        p1 = p1.next
        p2 = p2.next
    return p2


# solution by lubula
# 返回链表的倒数第 k 个节点
def findFromEnd(head: ListNode, k: int) -> ListNode:
    p1 = head
    # p1 先走 k 步
    for i in range(k):
        p1 = p1.next
    p2 = head
    # p1 和 p2 同时走 n - k 步
    while p1 != None:
        p2 = p2.next
        p1 = p1.next
    # p2 现在指向第 n - k + 1 个节点，即倒数第 k 个节点
    return p2
