// https://leetcode.cn/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150
import { ListNode } from "./models";

export function hasCycle(head: ListNode | null): boolean {
    if (head === null) {
        return false;
    } else {
        let slow: ListNode = head;
        let fast: ListNode | null = head.next;
        while (slow !== fast) {
            if (fast === null || fast.next === null) {
                return false;
            } else {
                slow = slow.next as ListNode;
                fast = fast.next.next;
            }
        }
        return true;
    }
};
