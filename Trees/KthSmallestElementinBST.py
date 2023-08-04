# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inorder(root, lst):
            if root is None:
                return
            inorder(root.left, lst)
            lst.append(root.val)
            inorder(root.right, lst)
        
        inorder(root, res)
        return res[k-1]

        