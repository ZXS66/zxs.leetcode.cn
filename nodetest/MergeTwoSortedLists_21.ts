// https://leetcode.cn/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150

import { ListNode } from "./models";

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    const head = new ListNode(0);
    let cur = head;
    let cur1 = list1, cur2 = list2;
    while (cur1 && cur2) {
        if (cur1.val < cur2.val) {
            cur.next = cur1;
            cur1 = cur1.next;
        } else {
            cur.next = cur2;
            cur2 = cur2.next;
        }
        cur = cur.next;
    }
    cur.next = cur1 ? cur1 : cur2;
    return head.next;
};

export default mergeTwoLists;