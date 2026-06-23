# 自己实现的 优先队列，二叉堆
from collections import deque


class MyPriorityQueue:
    arr:deque
    def __init__(self):
        self.arr = deque()
        

     # 返回队列中的元素个数
    def size(self) -> int:
        return len(self.arr)


    # 向队列中插入一个元素
    def push(self, x: int):
        self.arr.append(x)
        self.swim(len(self.arr)-1)
        pass

    # 上升
    def swim(self, index:int):
        p = self.parent(index)
        while p>=0:
            if(self.arr[index]<self.arr[p]):
                self.arr[p],self.arr[index]=self.arr[index],self.arr[p]
                index = p 
                p = self.parent(index)                
            else:
                break

    # 下沉
    def sink_problem(self):
        index = 0
        length = len(self.arr)
        while self.left(index)<=length-1:
            left_index = self.left(index)
            right_index = self.right(index)
            # 有问题，要和最小的孩子交换,例如 [9,5,4]，交换后为[5,9,4],不符合最小堆的定义
            #要从【原父节点】、【左孩子】、【右孩子】这三个数中，选出一个数放到【父节点】的位置。
            # 为了满足最小堆的定义，这个新选出来的【父节点】，必须是这三个数中最小的那一个。
            if(left_index<=length-1 and  self.arr[index]>self.arr[left_index]):
                self.arr[index],self.arr[left_index] = self.arr[left_index],self.arr[index]
                index = left_index
                continue
            if right_index<=length-1 and self.arr[index]>self.arr[right_index]:
                self.arr[index],self.arr[right_index] = self.arr[right_index],self.arr[index] 
                index = right_index
                continue
            break
    

    # 下沉
    def sink(self):
        index = 0
        length = len(self.arr)
        while self.left(index) < length:          # 存在左孩子才循环
            left = self.left(index)
            right = self.right(index)
            # 找到更小的孩子
            smaller = left
            if right < length and self.arr[right] < self.arr[left]:
                smaller = right
            # 如果父节点大于较小的孩子，则交换，否则结束
            if self.arr[index] > self.arr[smaller]:
                self.arr[index], self.arr[smaller] = self.arr[smaller], self.arr[index]
                index = smaller
            else:
                break

    # 返回队列中的最小元素（堆顶元素）
    def peek(self) -> int:
        return self.arr[0]
        

    # 删除并返回队列中的最小元素（堆顶元素）
    def pop(self) -> int:
        a = self.arr.popleft()
        if(self.is_empty()):
            return a 
        max = self.arr.pop()
        self.arr.appendleft(max)
        self.sink()
        return a

    # 父节点的索引
    def parent(self,index: int) -> int:
        return (index - 1) // 2

    # 左子节点的索引
    def left(self,index: int) -> int:
        return index * 2 + 1

    # 右子节点的索引
    def right(self,index: int) -> int:
        return index * 2 + 2
    #是否为空
    def is_empty(self):
        return len(self.arr)<=0
    
    