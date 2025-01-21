# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans
        if root.left is not None:
            ans = self.postorderTraversal(root.left)
        if root.right is not None:
            ans += self.postorderTraversal(root.right)
        ans.append(root.val)
        return ans
        