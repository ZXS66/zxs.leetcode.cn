// https://leetcode.cn/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
    const sumValOfFirst = (l1?.val ?? 0) + (l2?.val ?? 0);
    const sum = new ListNode(sumValOfFirst % 10);
    let n = sum;
    let n1 = l1?.next;
    let n2 = l2?.next;
    let surplus = (sumValOfFirst >= 10);
    while (n1 || n2) {
        const val = (n1?.val ?? 0) + (n2?.val ?? 0) + (surplus ? 1 : 0);
        const node = new ListNode(val % 10);
        n.next = node;
        n1 = n1?.next;
        n2 = n2?.next;
        surplus = (val >= 10);
        n = n.next;
    }
    if (surplus) {
        n.next = new ListNode(1);
    }
    return sum;
};
