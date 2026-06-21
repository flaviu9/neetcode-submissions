# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = []
        stack2 = []
        res1 = []
        res2 = []
        curr1 = p
        curr2 = q

        while curr1 or curr2 or stack1 or stack2:
            while curr1 or curr2:
                stack1.append(curr1)
                stack2.append(curr2)
                if (curr1.left is None) != (curr2.left is None):
                    return False
                else:
                    curr1 = curr1.left
                    curr2 = curr2.left
            curr1 = stack1.pop()
            curr2 = stack2.pop()
            res1.append(curr1.val)
            res2.append(curr2.val)
            curr1 = curr1.right
            curr2 = curr2.right
        return res1 == res2
