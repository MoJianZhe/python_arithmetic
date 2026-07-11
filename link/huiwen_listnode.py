# 二叉树遍历框架
def traverse(root: TreeNode) -> None:
    # 前序遍历代码
    traverse(root.left)
    # 中序遍历代码
    traverse(root.right)
    # 后序遍历代码


# 递归遍历单链表
def traverse(head: ListNode) -> None:
    # 前序遍历代码
    traverse(head.next)
    # 后序遍历代码


# 234. 回文链表
class Solution:
    # 从左向右移动的指针
    left = None

    # 记录链表是否为回文
    res = True

    def isPalindrome(self, head: ListNode) -> bool:
        self.left = head
        self.traverse(head)
        return self.res

    def traverse(self, right: ListNode):
        if right is None:
            return

        # 利用递归，走到链表尾部
        self.traverse(right.next)

        # 后序遍历位置，此时的 right 指针指向链表右侧尾部
        # 所以可以和 left 指针比较，判断是否是回文链表
        if self.left.val != right.val:
            self.res = False
        self.left = self.left.next
