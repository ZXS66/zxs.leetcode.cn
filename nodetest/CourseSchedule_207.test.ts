// https://leetcode.cn/problems/course-schedule/description/?envType=study-plan-v2&envId=top-interview-150

function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    // build the graph
    /** `graph[bi][ai]`: `bi` is a prerequisite of `ai` (bi → ai) */
    const graph: number[][] = Array.from({ length: numCourses }, () => []);
    const prereqNums = Array(numCourses).fill(0);
    for (const [ai, bi] of prerequisites) {
        // prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi (bi → ai)
        graph[bi].push(ai);
        prereqNums[ai]++;
    }
    const queue: number[] = [];
    for (let i = 0; i < numCourses; i++) {
        if (!prereqNums[i]) {
            // 0 prerequisites (can be finished)
            queue.push(i);
        }
    }
    let finishNum = 0;
    while (queue.length) {
        const cur = queue.pop()!;
        finishNum++;
        for (const next of graph[cur]) {
            prereqNums[next]--;
            if (!prereqNums[next]) {
                queue.push(next);
            }
        }
    }
    return finishNum === numCourses;
};



// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { numCourses: 2, prerequisites: [[1, 0]], result: true },
    { numCourses: 2, prerequisites: [[1, 0], [0, 1]], result: false },
    { numCourses: 7, prerequisites: [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]], result: true },
];

describe.each(testcases)(`numCourses: $numCourses, prerequisites:$prerequisites`, ({ numCourses, prerequisites, result }) => {
    test(`returns ${result}`, () => {
        expect(canFinish(numCourses, prerequisites)).toBe(result);
    });
});
