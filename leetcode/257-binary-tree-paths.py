# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        def _dfs(n: TreeNode, path: str):
            if not n:
                return
            
            if not path or len(path) == 0:
                path = str(n.val)
            else:
                path += f"->{n.val}"
            
            if not n.left and not n.right:
                ans.append(path)
            else:
                _dfs(n.left, path)
                _dfs(n.right, path)
                
        _dfs(root, None)
        return ans
            