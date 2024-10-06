// https://leetcode.cn/problems/zigzag-conversion/?envType=study-plan-v2&envId=top-interview-150


function convert(s: string, numRows: number): string {
    if (numRows === 1) return s;

    const rows: string[] = new Array(numRows).fill("");
    let row = 0;
    let goingDown = false;

    for (const char of s) {
        rows[row] += char;
        if (row === 0 || row === numRows - 1) goingDown = !goingDown;
        row += goingDown ? 1 : -1;
    }

    return rows.join("");
};


// unit test
import { describe, expect, test } from '@jest/globals';

const testcases = [
    { s: "PAYPALISHIRING", numRows: 3, result: "PAHNAPLSIIGYIR" },
    { s: "PAYPALISHIRING", numRows: 4, result: "PINALSIGYAHRPI" },
    { s: "A", numRows: 1, result: "A" },
];

describe.each(testcases)(`s:$s, numRows:$numRows`, ({ s, numRows, result }) => {
    test(`returns`, () => {
        expect(convert(s, numRows)).toBe(result);
    });
});
