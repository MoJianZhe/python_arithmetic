from binary_tree.graph_console import print_tree_top_down
from double_point import delete_repeat_node
from link import list_node
from link import reverse_link_node
from small_beautiful.car_pooling import Solution

if __name__ == "__main__":
    # print("打印树结构 1:")
    # tree1 = tree_node.build_tree_from_list([1, 2, 3, None, None, 4, 5])
    # print_tree_top_down(tree1)

    # list = [1,1,1,2,3]
    # list = [1,2,3,3,4,4,5]
    # list = [1,1]
    a = Solution()
    r = a.carPooling([[2,1,5],[3,5,7]],3)
    print(r)
    # r2 = a.carPooling([[2,1,5],[3,3,7]],4)
    # print(r2)
