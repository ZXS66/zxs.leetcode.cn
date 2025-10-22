# https://leetcode.cn/problems/binary-tree-preorder-traversal/description/
from typing import List, Optional

from _models import TreeNode

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None or root.val is None:
            return []
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return [root.val] + left + right
    