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

// unit test

import { describe, expect, test } from '@jest/globals';
import { genListNode, fmtListNode } from './utilities';

const testcases = [
    { l1: [1, 2, 4], l2: [1, 3, 4], result: [1, 1, 2, 3, 4, 4] },
    { l1: [], l2: [], result: [] },
    { l1: [], l2: [0], result: [0] },
];

describe.each(testcases)(`l1: $l1, l2: $l2`, ({ l1, l2, result }) => {
    test(`returns ${result}`, () => {
        const ln1 = genListNode(l1);
        const ln2 = genListNode(l2);
        const value = mergeTwoLists(ln1, ln2);
        // expect(value).toBe(result);
        expect(fmtListNode(value)).toEqual(JSON.stringify(result));
    });
});
