# 反转以 head 为起点的单链表
from link.list_node import ListNode


def reverseList(self, head: ListNode) -> ListNode:
    p = head 
    while p.next:
        new = p.next 
        temp = p
        new.next = temp
       # 注意：p = p.next 此时会造成死循环，因为上面的 new.next = temp 已经改变了链表结构
        p = p.next
    head.next = None
    return p 

def reverseList2( head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    cur = head
    pre = ListNode(None) # 不能用这个，翻转后死循环了
    pre.next = cur 
    after = cur.next
    # 最后一次 after (after为空的前一次)，after的指向没有指向 cur ,
    # 导致没有连接出来。
    while after:
        cur.next = pre 
        pre = cur 
        cur = after
        after = after.next
    return cur 

# 反转以 head 为起点的单链表
# laubla
def reverseList(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    # 由于单链表的结构，至少要用三个指针才能完成迭代反转
    # cur 是当前遍历的节点，pre 是 cur 的前驱结点，nxt 是 cur 的后继结点
    pre, cur, nxt = None, head, head.next
    while cur is not None:
        # 逐个结点反转
        cur.next = pre
        # 更新指针位置
        pre = cur
        cur = nxt
        if nxt is not None:
            nxt = nxt.next
    # 返回反转后的头结点
    return pre


# AI写法
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    pre = None       # 反转后的尾节点必须指向 None
    cur = head
    
    while cur:
        after = cur.next  # 1. 暂存下一个节点
        cur.next = pre    # 2. 反转当前节点的箭头
        pre = cur         # 3. pre 往前走一步
        cur = after       # 4. cur 往前走一步
        
    return pre      