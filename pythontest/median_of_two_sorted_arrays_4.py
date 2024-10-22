# https://leetcode.cn/problems/median-of-two-sorted-arrays/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        combined = sorted(nums1+nums2)
        m_plus_n = m+n
        return (combined[(m_plus_n-1)//2]+combined[m_plus_n//2])/2 if m_plus_n%2==0 else combined[(m_plus_n-1)//2]
        