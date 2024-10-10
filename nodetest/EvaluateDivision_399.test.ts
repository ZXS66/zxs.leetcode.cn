// https://leetcode.cn/problems/evaluate-division/description/?envType=study-plan-v2&envId=top-interview-150

function calcEquation(equations: string[][], values: number[], queries: string[][]): number[] {
    const n = equations.length;
    /** 有向图，[Ai, [Bi, multiply]] */
    const graph: Map<string, Map<string, number>> = new Map();
    for (let i = 0; i < n; i++) {
        const [Ai, Bi] = equations[i];
        const val = values[i];
        if (!graph.has(Ai)) graph.set(Ai, new Map());
        if (!graph.has(Bi)) graph.set(Bi, new Map());
        // Ai / Bi = values[i]
        graph.get(Ai)!.set(Bi, val);
        graph.get(Bi)!.set(Ai, 1 / val);
    }
    const getQueryResult = (Ci: string, Di: string): number => {
        const visited: Set<string> = new Set();
        const dfs = (node: string): number => {
            if (node === Di) return 1;
            visited.add(node);
            for (const [neighbor, val] of graph.get(node)!.entries()) {
                if (!visited.has(neighbor)) {
                    const res = dfs(neighbor);
                    if (res !== -1) return val * res;
                }
            }
            return -1;
        }
        return dfs(Ci);
    };
    const ans: number[] = [];
    for (const [Ci, Di] of queries) {
        if (!graph.has(Ci) || !graph.has(Di)) ans.push(-1);
        else if (Ci === Di) ans.push(1);
        else {
            ans.push(getQueryResult(Ci, Di));
        }
    }
    return ans;
};


// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { equations: [["a", "b"], ["b", "c"]], values: [2.0, 3.0], queries: [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]], result: [6.00000, 0.50000, -1.00000, 1.00000, -1.00000] },
    { equations: [["a", "b"], ["b", "c"], ["bc", "cd"]], values: [1.5, 2.5, 5.0], queries: [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]], result: [3.75000, 0.40000, 5.00000, 0.20000] },
    { equations: [["a", "b"]], values: [0.5], queries: [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]], result: [0.50000, 2.00000, -1.00000, -1.00000] },
];

describe.each(testcases)(`equations: $equations, values:$values, queries:$queries`, ({ equations, values, queries, result }) => {
    test(`returns ${result}`, () => {
        expect(calcEquation(equations, values, queries)).toEqual(result);
    });
});