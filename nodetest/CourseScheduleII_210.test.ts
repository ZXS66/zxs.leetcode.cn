// https://leetcode.cn/problems/course-schedule-ii/description/?envType=study-plan-v2&envId=top-interview-150

function findOrder(numCourses: number, prerequisites: number[][]): number[] {
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
    const ans: number[] = [];
    let finishNum = 0;
    while (queue.length) {
        const cur = queue.pop()!;
        ans.push(cur);
        finishNum++;
        for (const next of graph[cur]) {
            prereqNums[next]--;
            if (!prereqNums[next]) {
                queue.push(next);
            }
        }
    }
    if (finishNum === numCourses) {
        return ans;
    } else {
        // 如果不可能完成所有课程，返回一个空数组。
        return [];
    }
};



// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { numCourses: 2, prerequisites: [[1, 0]], result: [0, 1] },
    { numCourses: 4, prerequisites: [[1, 0], [2, 0], [3, 1], [3, 2]], result: [0, 2, 1, 3] },
    { numCourses: 1, prerequisites: [], result: [0] },
];

describe.each(testcases)(`numCourses: $numCourses, prerequisites:$prerequisites`, ({ numCourses, prerequisites, result }) => {
    test(`returns ${result}`, () => {
        expect(findOrder(numCourses, prerequisites)).toEqual(result);
    });
});
