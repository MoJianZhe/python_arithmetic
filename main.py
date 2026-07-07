
from link import list_node
from link.list_node import ListNode
from my_array.priority_queue import MyPriorityQueue
from binary_tree import tree_node
from binary_tree.graph_console import print_tree_top_down
from double_point.merge_k_list import Solution

if __name__=='__main__':
    # print("打印树结构 1:")
    # tree1 = tree_node.build_tree_from_list([1, 2, 3, None, None, 4, 5])
    # print_tree_top_down(tree1)
    
    a = Solution()
    lists = [[1,4,5],[1,3,4],[2,6]]
    ll = []
    for l in lists:
        head = list_node.array_to_linked_list(l)
        ll.append(head)
    r = a.mergeKLists(ll)
    list_node.print_linked_list(r)

