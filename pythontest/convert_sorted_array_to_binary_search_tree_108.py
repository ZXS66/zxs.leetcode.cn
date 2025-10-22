# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/?envType=study-plan-v2&envId=top-interview-150

from math import sqrt
from typing import Optional

from _models import TreeNode

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        n = len(nums)
        # depth = int(sqrt(0.25+2*n)-0.5)
        rootVal = nums[n // 2]
        left, right = nums[: n // 2], nums[n // 2 + 1 :]
        return self.buildBST(rootVal, left, right)

    def buildBST(self, rootVal: int, left: list[int], right: list[int]) -> TreeNode:
        root = TreeNode(rootVal)
        if left is not None and len(left) > 0:
            root.left = self.buildBST(
                left[len(left) // 2], left[: len(left) // 2], left[len(left) // 2 + 1 :]
            )
        if right is not None and len(right) > 0:
            root.right = self.buildBST(
                right[len(right) // 2],
                right[: len(right) // 2],
                right[len(right) // 2 + 1 :],
            )
        return root
