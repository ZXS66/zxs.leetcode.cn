// https://leetcode.cn/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150
import { ListNode } from "./models";

function hasCycle(head: ListNode | null): boolean {
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

// unit test
import { describe, expect, test } from '@jest/globals';
import { genListNode } from "./utilities";

const testcases = [
    { head: [3, 2, 0, 4, 0], pos: 1, result: true },
    { head: [1, 2, 1], pos: 0, result: true },
    { head: [1], pos: -1, result: false },
];

describe.each(testcases)(`head: $head, result: $result`, ({ head, pos, result }) => {
    test(`returns`, () => {
        const theTree = genListNode(head);
        if (pos !== -1) {
            let theNode: ListNode | null = null;
            let cur = theTree;
            let idx = 0;
            while (cur !== null && cur.next != null) {
                if (idx === pos) {
                    theNode = cur;
                }
                idx++;
                cur = cur.next;
            }
            cur!.next = theNode;
        }
        expect(hasCycle(theTree)).toBe(result);
    });
});
