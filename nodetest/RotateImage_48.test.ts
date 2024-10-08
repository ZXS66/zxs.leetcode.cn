// https://leetcode.cn/problems/rotate-image/?envType=study-plan-v2&envId=top-interview-150

/**
 Do not return anything, modify matrix in-place instead.
 */
function rotate(matrix: number[][]): void {
    const n = matrix.length;
    if (n === 1) return;
    const odd = n % 2 === 1;
    const point = Math.floor(n / 2);
    for (let i = 0; i < n / 2; i++) {
        if (odd && i === point) {
            continue;
        }
        for (let j = 0; j < n / 2; j++) {
            const temp = matrix[i][j];
            matrix[i][j] = matrix[n - 1 - j][i];
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j];
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i];
            matrix[j][n - 1 - i] = temp;
        }
    }
};

// unit test
import { describe, expect, test } from '@jest/globals';

const testcases = [
    {
        matrix: [[1]],
        result: [[1]]
    },
    {
        matrix: [[1, 2], [3, 4]],
        result: [[3, 1], [4, 2]]
    },
    {
        matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        result: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    },
    {
        matrix: [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
        result: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    },
    {
        matrix: [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],
        result: [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]]
    }
];

describe.each(testcases)(`matrix:$matrix`, ({ matrix, result }) => {
    test(`returns ${result}`, () => {
        rotate(matrix);
        expect(JSON.stringify(matrix)).toEqual(JSON.stringify(result));
    });
});
