# 23.合并k个有序的链表 
import heapq
from typing import List, Optional

from link.list_node import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vir = ListNode(None)
        r = vir
        pq = []
        for i, heap in enumerate(lists):
            if heap is not None:
                heapq.heappush(pq, (heap.val, i, heap))

        while len(pq) > 0:
            a, b, heap = heapq.heappop(pq)
            if heap.next is not None:
                heapq.heappush(pq, (heap.next.val, b, heap.next))
            r.next = heap
            r = r.next

        return vir.next

    # labula solution
    def mergeKLists(self, lists):
        if not lists:
            return None
        # 虚拟头结点
        dummy = ListNode(-1)
        p = dummy
        # 优先级队列，最小堆
        pq = []
        # 将 k 个链表的头结点加入最小堆
        for i, head in enumerate(lists):
            if head is not None:
                heapq.heappush(pq, (head.val, i, head))

        while pq:
            # 获取最小节点，接到结果链表中
            val, i, node = heapq.heappop(pq)
            p.next = node
            if node.next is not None:
                heapq.heappush(pq, (node.next.val, i, node.next))
            # p 指针不断前进
            p = p.next

        return dummy.next
