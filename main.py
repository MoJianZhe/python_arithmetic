
from binary_tree.graph_console import print_tree_top_down
from double_point.merge_k_list import Solution
from double_point import delete_repeat_node
from link import list_node


if __name__=='__main__':
    # print("打印树结构 1:")
    # tree1 = tree_node.build_tree_from_list([1, 2, 3, None, None, 4, 5])
    # print_tree_top_down(tree1)
    
    # list = [1,1,1,2,3]
    # list = [1,2,3,3,4,4,5]
    list = [1,1]
    head = list_node.array_to_linked_list(list)
    a = delete_repeat_node.deleteDuplicatesOther(None,head)
    list_node.print_linked_list(a)

