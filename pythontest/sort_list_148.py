# Definition for singly-linked list.
from collections import defaultdict
from typing import Optional

from _models import ListNode


def buildListNode_148(nums: list[int]) -> Optional[ListNode]:
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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        store = defaultdict(list)
        curr = head
        while curr:
            store[curr.val].append(curr)
            curr = curr.next

        keys = sorted(list(store.keys()))
        for k in keys:
            nodes = store[k]
            if curr:
                curr.next = nodes[0]
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
            curr = nodes[-1]
        
        if len(keys) == 0:
            return None
        if curr is not None:
            curr.next = None
        return store[keys[0]][0]

        # 方案二：超时
        # curr = head
        # while curr:
        #     if curr.next and curr.val > curr.next.val:
        #         curr.val, curr.next.val = curr.next.val, curr.val
        #         curr = head
        #     else:
        #         curr = curr.next

        # return head
