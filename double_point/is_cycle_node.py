# 节点是否成环
# 快慢指针初始化指向 head
from link.list_node import ListNode


def hasCycle(self, head: ListNode) -> bool:
    fast = head
    low = head
    while fast is not None and fast.next is not None:
        low = low.next
        fast = fast.next.next
        if fast == low:
            return True
    return False


# 快慢指针初始化指向 head
# labula solution
def hasCycle(self, head: ListNode) -> bool:
    slow = head
    fast = head
    # 快指针走到末尾时停止
    while fast is not None and fast.next is not None:
        # 慢指针走一步，快指针走两步
        slow = slow.next
        fast = fast.next.next
        # 快慢指针相遇，说明含有环
        if slow == fast:
            return True
    # 不包含环
    return False

# 在环的场景，fast 走两步，如果fast 刚好跳过了 low 呢？不也遇不到了么？
'''
不会跳过。这是很多初学者的直觉误区，我们可以用相对速度来理解。

1. 为什么不会“跳过”？
想象一下操场跑圈：

slow 每次走 1 步。
fast 每次走 2 步。
相对速度：fast 相对于 slow，每次只靠近 1 步。
在环里，它们就像是在一个圆形跑道上跑步。因为 fast 比 slow 快，所以 fast 是从后面追 slow 的。 既然每次只靠近 1 步，那么它们之间的距离变化是这样的： 距离3 -> 距离2 -> 距离1 -> 距离0 (相遇)

它不可能从“距离1”直接变成“距离-1”（即跳过），因为每一步只缩小 1 个单位的距离。只要它们在环里，fast 一定会一步一步地逼近 slow，直到重合。

2. 数学证明（简单版）
假设在某一时刻，fast 和 slow 在环里的距离是 
d
d（
d
d 是环长的一部分）。

下一轮循环后，slow 走了 1 步，fast 走了 2 步。
它们之间的距离变成了 
d
−
1
d−1。
再下一轮，距离变成 
d
−
2
d−2。
...
最终距离一定会变成 
0
0，也就是相遇。
即使 fast 在 slow 后面很远，它也只是多转几圈的问题，最终一定会以“每次接近 1 步”的速度追上 slow。

3. 如果 fast 走 3 步会怎样？
如果你把代码改成 fast = fast.next.next.next（每次走 3 步），那就有可能永远遇不到！

此时相对速度是 2 步。
如果环的长度是偶数，且初始距离是奇数，那么距离变化会是：奇数 -> 奇数-2=奇数 -> ... -> 1 -> -1 (跳过)。
这时候就会发生你担心的“跳过”现象，导致死循环或者需要更复杂的判断。
但在本题中，快指针走 2 步，慢指针走 1 步，相对速度为 1，保证了绝对能相遇。


'''