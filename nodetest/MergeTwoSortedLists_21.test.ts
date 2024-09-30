import { describe, expect, test } from '@jest/globals';
import mergeTwoLists from './MergeTwoSortedLists_21';
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
