// https://leetcode.cn/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
    if (head === null) {
        return false;
    } else {
        let slow = head;
        let fast = head.next;
        while (slow !== fast) {
            if (fast === null || fast.next === null) {
                return false;
            } else {
                slow = slow.next;
                fast = fast.next.next;
            }
        }
        return true;
    }
};
