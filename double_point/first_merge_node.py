# 142.单链表，环的第一个交点
# 1、直接用一个hashset ,一个指针遍历，看是否有重复的。
from link.list_node import ListNode

# 解法二，快，慢指针相交之后，将low指向头节点，让它们继续走(按相同速度），再次相遇的点，就是第一个交点
def detectCycle(self, head: ListNode):
    fast = head
    low = head 
    while fast is not None and fast.next is not None:
        low = low.next
        fast = fast.next.next
        if low == fast :
            break
    if(fast is None or fast.next is None):
        return None
    
    low = head
    while low is not None:
        if low == fast :
            break
        low = low.next 
        fast = fast.next
        # 应该先判断是否相等，再走。可能就是再原点相交。
        # if low == fast : 
        #     break
    return low 
        

# solution by labula 
def detectCycle(self, head: ListNode):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    
    # 上面的代码类似 hasCycle 函数
    if not fast or not fast.next:
        # fast 遇到空指针说明没有环
        return None
    
    # 重新指向头结点
    slow = head 
    # 快慢指针同步前进，相交点就是环起点
    while slow != fast:
        fast = fast.next
        slow = slow.next
    return slow