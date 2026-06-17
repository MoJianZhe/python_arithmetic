from collections import deque
from binary_tree.tree_node import TreeNode
from binary_tree import tree_node

def print_tree_top_down(root: TreeNode):
    """
    正向打印二叉树（自顶向下）
    """
    def build_str_blocks(node):
        """
        递归构建二维字符块
        返回: lines(行列表), width(宽度), height(高度), mid(根节点中心位置)
        """
        if node is None:
            return [], 0, 0, 0

        # 转为字符串
        val_str = str(node.val)
        val_len = len(val_str)

        # 1. 只有根节点（叶子节点）
        if node.left is None and node.right is None:
            return [val_str], val_len, 1, val_len // 2

        # 2. 只有左孩子
        if node.right is None:
            lines, width, height, mid = build_str_blocks(node.left)
            first_line = (mid + 1) * ' ' + (width - mid - 1) * '_' + val_str
            second_line = mid * ' ' + '/' + (width - mid - 1 + val_len) * ' '
            shifted_lines = [line + val_len * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, width + val_len, height + 2, width + val_len // 2

        # 3. 只有右孩子
        if node.left is None:
            lines, width, height, mid = build_str_blocks(node.right)
            first_line = val_str + mid * '_' + (width - mid) * ' '
            second_line = (val_len + mid) * ' ' + '\\' + (width - mid - 1) * ' '
            shifted_lines = [val_len * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, width + val_len, height + 2, val_len // 2

        # 4. 左右孩子都有
        left_lines, left_w, left_h, left_mid = build_str_blocks(node.left)
        right_lines, right_w, right_h, right_mid = build_str_blocks(node.right)

        first_line = (left_mid + 1) * ' ' + (left_w - left_mid - 1) * '_' + val_str + right_mid * '_' + (right_w - right_mid) * ' '
        second_line = left_mid * ' ' + '/' + (left_w - left_mid - 1 + val_len + right_mid) * ' ' + '\\' + (right_w - right_mid - 1) * ' '

        # 如果左右子树高度不同，用空格补齐较低的一边
        if left_h < right_h:
            left_lines += [left_w * ' '] * (right_h - left_h)
        elif right_h < left_h:
            right_lines += [right_w * ' '] * (left_h - right_h)

        # 左右子树拼接在一行
        zipped_lines = [l + val_len * ' ' + r for l, r in zip(left_lines, right_lines)]
        
        return [first_line, second_line] + zipped_lines, left_w + right_w + val_len, max(left_h, right_h) + 2, left_w + val_len // 2

    # 执行并打印
    lines, *_ = build_str_blocks(root)
    for line in lines:
        print(line)



