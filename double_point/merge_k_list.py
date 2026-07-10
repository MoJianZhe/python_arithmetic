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


#378. 有序矩阵中第 K 小的元素
def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    # 存储二元组 (matrix[i][j], i, j)
    # i, j 记录当前元素的索引位置，用于生成下一个节点
    pq = PriorityQueue()

    # 初始化优先级队列，把每一行的第一个元素装进去
    for i in range(len(matrix)):
        pq.put((matrix[i][0], i, 0))

    res = -1
    # 执行合并多个有序链表的逻辑，找到第 k 小的元素
    while not pq.empty() and k > 0:
        cur = pq.get()
        # 按照元素大小升序排序
        res = cur[0]
        k -= 1
        # 链表中的下一个节点加入优先级队列
        i, j = cur[1], cur[2]
        if j + 1 < len(matrix[i]):
            pq.put((matrix[i][j + 1], i, j + 1))
    return res