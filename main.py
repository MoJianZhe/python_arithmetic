
from binary_tree import tree_node
from binary_tree.graph_console import print_tree_top_down


if __name__=='__main__':
    print("测试用例 1:")
    tree1 = tree_node.build_tree_from_list([1, 2, 3, None, None, 4, 5])
    print_tree_top_down(tree1)
    
    print("\n" + "="*40 + "\n")

    print("测试用例 2:")
    tree2 = tree_node.build_tree_from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    print_tree_top_down(tree2)
    pass
