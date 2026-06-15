from collections import deque
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

if __name__=='__main__':
    a = deque([1,2,3])
    print(a.popleft())
    pass