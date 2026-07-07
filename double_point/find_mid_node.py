# 查找链表上的中间节点，因为不知道节点后续有多少个，所以不要求n
from link.list_node import ListNode


def middleNode(self, head: ListNode) -> ListNode:
    fast = head
    low = head
    while fast is not None and fast.next is not None:
        low = low.next
        fast = fast.next.next
    return low

    # 快慢指针初始化指向 head
def middleNode(self, head: ListNode) -> ListNode:
    slow = head
    fast = head
    # 快指针走到末尾时停止
    while fast is not None and fast.next is not None:
        # 慢指针走一步，快指针走两步
        slow = slow.next
        fast = fast.next.next
    # 慢指针指向中点
    return slow