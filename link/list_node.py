class ListNode:
    """链表"""

    def __init__(self, val):
        self.val = val
        self.next = None

def array_to_linked_list(arr):
    """
    将数组转换为单向链表
    :param arr: List[]
    :return: ListNode (链表的头节点)
    """
    # 如果数组为空，返回 None
    if not arr:
        return None
    
    # 创建一个虚拟头节点(dummy node)，方便统一处理
    dummy = ListNode(0)
    current = dummy
    
    # 遍历数组，依次创建节点并链接
    for val in arr:
        current.next = ListNode(val)
        current = current.next
        
    # 返回真正的头节点（虚拟头节点的下一个节点）
    return dummy.next

def print_linked_list(head):
    """
    辅助函数：打印链表，方便验证结果
    """
    elements = []
    current = head
    while current:
        elements.append(str(current.val))
        current = current.next
    print(" -> ".join(elements))