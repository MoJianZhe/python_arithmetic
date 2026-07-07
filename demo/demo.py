


from collections import deque
import heapq
import itertools


if __name__ == '__main__':
    p = [3,2,1,24,32,22,2]
    heapq.heapify(p) 
    while(len(p)>0):
        a = heapq.heappop(p)
        print(a)
    print("结束")

    a = []
    heapq.heappush(a,2)
    heapq.heappush(a,3)
    heapq.heappush(a,10)
    heapq.heappush(a,12)
    while(len(a)>0):
        m = heapq.heappop(a)
        print(m)
    print(f"'打印a 结束'")

    b = []
    counter = itertools.count()
    heapq.heappush(b,(1,next(counter),"diyige"))
    heapq.heappush(b,(3,next(counter),"dierge"))
    heapq.heappush(b,(2,next(counter),"disange"))
    heapq.heappush(b,(2,next(counter),"di四ge"))
    while len(b)>0:
        yuanzu = heapq.heappop(b)
        print(yuanzu)
    print("打印元组结束")
