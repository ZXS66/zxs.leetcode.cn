// https://leetcode.cn/problems/clone-graph/description/?envType=study-plan-v2&envId=top-interview-150


/** Definition for _Node. */
class _Node {
    val: number
    neighbors: _Node[]

    constructor(val?: number, neighbors?: _Node[]) {
        this.val = (val === undefined ? 0 : val)
        this.neighbors = (neighbors === undefined ? [] : neighbors)
    }
}

function cloneGraph(node: _Node | null): _Node | null {
    if (!node) return null;
    const clonedNodes = new Map<number, _Node>();
    const queue = [node];
    while (queue.length) {
        const cur = queue.shift()!;
        if (!clonedNodes.has(cur.val)) {
            clonedNodes.set(cur.val, new _Node(cur.val));
            for (const neighbor of cur.neighbors) {
                queue.push(neighbor);
            }
        }
    }
    queue.push(node);
    const visitedNodes = new Set();
    while (queue.length) {
        const cur = queue.shift()!;
        const clone = clonedNodes.get(cur.val)!;
        for (const neighbor of cur.neighbors) {
            const cloneNeighbor = clonedNodes.get(neighbor.val)!;
            if (!clone.neighbors.includes(cloneNeighbor)) {
                clone.neighbors.push(cloneNeighbor);
            }
            if (!visitedNodes.has(neighbor.val)) {
                visitedNodes.add(neighbor.val);
                queue.push(neighbor);
            }
        }
    }
    return clonedNodes.get(node.val)!;
};

// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { graph: [[2, 4], [1, 3], [2, 4], [1, 3]] },
    { graph: [[]] },
    { graph: [] },
];

function genNode(graph: number[][]): _Node | null {
    if (!Array.isArray(graph) || graph.length === 0) {
        return null;
    }
    const nodes = graph.map((_, i) => new _Node(i + 1));
    for (let i = 0; i < graph.length; i++) {
        nodes[i].neighbors = graph[i].map((j) => nodes[j - 1]);
    }
    return nodes[0];
}
function fmtNode(node: _Node) {
    if (!node) return "[]";
    const neighbors: number[][] = [];
    const queue = [node];
    while (queue.length) {
        const cur = queue.shift()!;
        if (!Array.isArray(neighbors[cur.val - 1])) {
            neighbors[cur.val - 1] = [];
        }
        for (const neighbor of cur.neighbors) {
            if (!neighbors[cur.val - 1].includes(neighbor.val)) {
                neighbors[cur.val - 1].push(neighbor.val);
                queue.push(neighbor);
            }
        }
    }
    return "[" + neighbors.map(item => "[" + item.join(',') + "]").join(',') + "]";
}

describe.each(testcases)(`graph: $graph`, ({ graph }) => {
    test(`returns`, () => {
        const node = genNode(graph!);
        const clone = cloneGraph(node);
        expect(fmtNode(clone!)).toBe(fmtNode(node!));
    });
});
