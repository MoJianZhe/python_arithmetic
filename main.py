from binary_tree.graph_console import print_tree_top_down
from double_point import delete_repeat_node
from link import list_node
from link import reverse_link_node
from small_beautiful.car_pooling import Solution
from binary_search.ship_with_days import ShipWithinDays

if __name__ == "__main__":
    # print("打印树结构 1:")
    # tree1 = tree_node.build_tree_from_list([1, 2, 3, None, None, 4, 5])
    # print_tree_top_down(tree1)

    # list = [1,1,1,2,3]
    # list = [1,2,3,3,4,4,5]
    # list = [1,1]
    a = ShipWithinDays()
    arr = [347,247,500,102,297,58,28,307,409,305,238,265,394,209,115,414,272,215,2,314,346,337,27,310]
    print(len(arr))
    b = a.find_day_by_result_bylabula(arr,500)
    print(b)
    # r2 = a.carPooling([[2,1,5],[3,3,7]],4)
    # print(r2)
