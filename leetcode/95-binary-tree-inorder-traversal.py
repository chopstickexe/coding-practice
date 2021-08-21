# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def _retrieve(n: TreeNode):
            if not n:
                return
            if n.left:
                _retrieve(n.left)
            ans.append(n.val)
            if n.right:
                _retrieve(n.right)
            
        _retrieve(root)
        return ans
    