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

if __name__=='__main__':
    pass