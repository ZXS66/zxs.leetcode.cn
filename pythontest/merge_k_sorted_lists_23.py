# https://leetcode.cn/problems/merge-k-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List, Optional

from _models import ListNode


def buildListNode(nums: list[int]) -> Optional[ListNode]:
    if nums is None or len(nums) == 0:
        return None
    else:
        head = ListNode(nums[0])
        curr = head
        for i in range(1, len(nums)):
            curr.next = ListNode(nums[i])
            curr = curr.next
        return head


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None
        k = len(lists)
        if k == 1:
            return lists[0]

        # 弹出最小值
        def pop_min():
            minIdx: int = -1
            minVal: int = 0
            # 找到 pointers 中，下一个最小值
            for i, v in enumerate(lists):
                if v is None:
                    continue
                if minIdx == -1 or v.val < minVal:
                    minIdx = i
                    minVal = v.val
            if minIdx == -1:
                return None
            minNode = lists[minIdx]
            if minNode is not None and minNode.next is not None:
                # 找到链表下一节点
                # 更新 pointers[minIdx] 为当前节点 (minNode) 的下一节点
                nextNode = minNode.next
                minNode.next = None
                lists[minIdx] = nextNode
            elif minIdx != -1:
                # 链表无下一节点
                del lists[minIdx]

            return minNode

        # 记忆最小 ListNode
        head = pop_min()
        if head is None:
            return None
        curr = head
        # 循环，直到 pointers 为空
        while True:
            minNode = pop_min()
            if curr is not None:
                curr.next = minNode
                curr = curr.next
            if minNode is None:
                break

        return head
