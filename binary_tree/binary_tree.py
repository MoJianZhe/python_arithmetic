from collections import deque
from typing import List
# 基本的二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 二叉树的递归遍历框架
def traverse(root: TreeNode):
    if root is None:
        return
    # print(root.val) # 前序 （中左右）
    traverse(root.left)
    print (root.val) # 中序 (左中右)
    traverse(root.right)
    # print(root.val) #后序 （左右中）

# BFS 层序遍历
def level_traverse(root:TreeNode):
    if(root is None):
        return
    node_list = []
    node_list.append(root)
    while(node_list.count>0):
        a:TreeNode = node_list.pop()
        if(a is None):
            continue
        node_list.append(a.left)
        node_list.append(a.right)        

# 标准写法
def levelOrderTraverse(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    # 记录当前遍历到的层数（根节点视为第 1 层）
    depth = 1

    while q:
        sz = len(q)
        for i in range(sz):
            cur = q.popleft()
            # 访问 cur 节点，同时知道它所在的层数
            print(f"depth = {depth}, val = {cur.val}")

            # 把 cur 的左右子节点加入队列
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
        depth += 1

#列表转换成树
def build_tree(arr:List[int])->TreeNode:
    if(arr is None or len(arr)<=0):
        return None
    size = len(arr)
    root = TreeNode(arr[0])
    i = 1
    queue = deque()
    queue.append(root)
    while(i < size):
        cur_node = queue.popleft();
        if(i < size):
            left = TreeNode(arr[i])
            cur_node.left = left
            queue.append(left)
            i +=1
        if(i < size):
            right = TreeNode(arr[i])
            cur_node.right = right
            queue.append(right)
            i +=1
    return root

# AI 写法
def build_tree_from_list(values: list) -> TreeNode:
    """
    将层序遍历的列表转换为二叉树
    例如: [1, 2, 3, None, None, 4, 5]
    """
    if not values or values[0] is None:
        return None

    # 1. 创建根节点
    root = TreeNode(values[0])
    # 2. 使用 deque 辅助构建
    queue = deque([root])
    
    # 3. i 用于遍历 values 列表，初始指向索引 1（即根节点的左孩子位置）
    i = 1
    n = len(values)

    while queue and i < n:
        # 弹出当前父节点
        node = queue.popleft()

        # 处理左孩子
        if i < n and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1  # 无论是不是 None，列表索引都要往前走

        # 处理右孩子
        if i < n and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root



if __name__=='__main__':
    a = [1,3,2,432,2,None,212]
    root = build_tree(a)
    levelOrderTraverse(root)
    print("=========结束1===========")
    levelOrderTraverse(build_tree_from_list(a))
    pass