// https://leetcode.cn/problems/destination-city/
function destCity(paths: string[][]): string {
    if (paths.length === 1) return paths[0][1];
    const set = new Set(paths.map(item => item[0]));
    for (const item of paths) {
        if (!set.has(item[1])) return item[1];
    }
    return "";
};


// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { paths: [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]], result: "Sao Paulo" },
    { paths: [["B", "C"], ["D", "B"], ["C", "A"]], result: "A" },
    { paths: [["A", "Z"]], result: "Z" },
];

describe.each(testcases)(`paths: $paths`, ({ paths, result }) => {
    test(`returns ${result}`, () => {
        expect(destCity(paths)).toBe(result);
    });
});
