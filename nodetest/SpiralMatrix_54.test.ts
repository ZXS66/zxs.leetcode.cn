// https://leetcode.cn/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-interview-150

function spiralOrder(matrix: number[][]): number[] {
    const m = matrix.length;
    const n = matrix[0].length;
    const res: number[] = [];
    let left = 0, right = n - 1, top = 0, bottom = m - 1;
    while (left <= right && top <= bottom) {
        for (let i = left; i <= right; i++) {
            res.push(matrix[top][i]);
        }
        for (let i = top + 1; i <= bottom; i++) {
            res.push(matrix[i][right]);
        }
        if (left < right && top < bottom) {
            for (let i = right - 1; i > left; i--) {
                res.push(matrix[bottom][i]);
            }
            for (let i = bottom; i > top; i--) {
                res.push(matrix[i][left]);
            }
        }
        left++;
        right--;
        top++;
        bottom--;
    }
    return res;
};

// unit test
import { describe, expect, test } from '@jest/globals';

const testcases = [
    {
        matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]], result: [1, 2, 3, 6, 9, 8, 7, 4, 5]
    },
    {
        matrix: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], result: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    }
];

describe.each(testcases)(`matrix:$matrix`, ({ matrix, result }) => {
    test(`returns ${result}`, () => {
        expect(spiralOrder(matrix)).toEqual(result);
    });
});
