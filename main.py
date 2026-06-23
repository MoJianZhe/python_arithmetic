
from my_array.priority_queue import MyPriorityQueue
from binary_tree import tree_node
from binary_tree.graph_console import print_tree_top_down


if __name__=='__main__':
    # print("打印树结构 1:")
    # tree1 = tree_node.build_tree_from_list([1, 2, 3, None, None, 4, 5])
    # print_tree_top_down(tree1)
    
    pq = MyPriorityQueue()
    pq.push(3)
    pq.push(1)
    pq.push(4)
    pq.push(1)
    pq.push(5)
    pq.push(9)
    # 1 1 3 4 5 9
    while not pq.is_empty():
        print(pq.pop())

