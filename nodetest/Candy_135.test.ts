// https://leetcode.cn/problems/candy/solutions/15204/fen-fa-tang-guo-by-powcai/?envType=study-plan-v2&envId=top-interview-150
function candy(ratings: number[]): number {
    // const myPrecious = new Array(ratings.length).fill(1);
    // const myPrecious = [1];
    // for (let i = 1; i < ratings.length; i++) {
    //     const rating = ratings[i];
    //     if (rating > ratings[i - 1]) {
    //         myPrecious[i] = myPrecious[i - 1] + 1;
    //     } else {
    //         myPrecious[i] = 1;
    //         if (rating < ratings[i - 1]) {
    //             let j = i - 1;
    //             while (j >= 0 && ratings[j] > ratings[j + 1]) {
    //                 if (myPrecious[j] < (myPrecious[j + 1] + 1)) {
    //                     myPrecious[j] = myPrecious[j + 1] + 1;
    //                 }
    //                 j--;
    //             }
    //         }
    //     }
    // }
    const n = ratings.length;
    const myPrecious: number[] = new Array(ratings.length).fill(1);
    for (let i = 1; i < n; i++) {
        if (ratings[i] > ratings[i - 1]) {
            myPrecious[i] = myPrecious[i - 1] + 1;
        }
    }
    let precious = myPrecious[n - 1], amount = myPrecious[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        precious = (ratings[i] > ratings[i + 1]) ? (precious + 1) : 1;
        amount += Math.max(precious, myPrecious[i]);
    }
    return amount;
};


// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { ratings: [1, 0, 2], result: 5 },
    { ratings: [1, 2, 2], result: 4 },
];

describe.each(testcases)(`ratings: $ratings`, ({ ratings, result }) => {
    test(`returns ${result}`, () => {
        expect(candy(ratings)).toBe(result);
    });
});
