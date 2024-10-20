# https://leetcode.cn/problems/search-a-2d-matrix/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            mid_val = matrix[mid // n][mid % n]
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
