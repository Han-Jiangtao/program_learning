# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.recurse(root)
        return self.ans

    def recurse(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        self.ans.append(root.val)
        self.recurse(root.left)
        self.recurse(root.right)
