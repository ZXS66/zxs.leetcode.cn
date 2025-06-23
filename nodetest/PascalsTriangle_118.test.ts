// https://leetcode.cn/problems/pascals-triangle/?envType=study-plan-v2&envId=top-100-liked

function generate(numRows: number): number[][] {
    const res: number[][] = [[1]];
    let row = 1;
    while (row < numRows) {
        res[row] = new Array(row + 1).fill(1);        
        for (let col = 1; col < row; col++) {
            res[row][col] = res[row - 1][col - 1] + res[row - 1][col];
        }
        row++;
    }
    return res;
};


// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { numRows: 5, result:[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]] },
    { numRows: 6, result:[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1]] },
    { numRows: 1, result: [[1]]},
];

describe.each(testcases)(`numRows: $numRows, result: $result`, ({ numRows, result }) => {
    test(`returns ${result}`, () => {
        const output = generate(numRows);
        expect(JSON.stringify(output)).toBe(JSON.stringify(result));
    });
});
