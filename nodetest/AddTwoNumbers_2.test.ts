// https://leetcode.cn/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150
import { ListNode } from "./models";

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode {
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

// unit tests
import { describe, expect, test } from '@jest/globals';
import { fmtListNode, genListNode } from './utilities';
const testcases = [
    { l1: [2, 4, 3], l2: [5, 6, 4], result: [7, 0, 8] },
    { l1: [0], l2: [0], result: [0] },
    { l1: [9, 9, 9, 9, 9, 9, 9], l2: [9, 9, 9, 9], result: [8, 9, 9, 9, 0, 0, 0, 1] }
];

describe.each(testcases)(`l1: $l1, l2: $l2`, ({ l1, l2, result }) => {
    test(`returns`, () => {
        const ln1 = genListNode(l1);
        const ln2 = genListNode(l2);
        const output = addTwoNumbers(ln1, ln2);
        const fmtResult = `[${result.join(",")}]`;
        expect(fmtListNode(output)).toBe(fmtResult);
    });
});
