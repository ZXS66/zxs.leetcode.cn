// https://leetcode.cn/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150

class RandomizedSet {
    __set: Set<number> = new Set();
    constructor() {
    }

    insert(val: number): boolean {
        if (this.__set.has(val)) {
            return false;
        } else {
            this.__set.add(val);
            return true;
        }
    }

    remove(val: number): boolean {
        if (this.__set.has(val)) {
            this.__set.delete(val);
            return true;
        } else {
            return false;
        }
    }

    getRandom(): number {
        return Array.from(this.__set)[Math.floor(Math.random() * this.__set.size)];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */



// unit test
import { describe, expect, test } from '@jest/globals';

describe(`O(1) 时间插入、删除和获取随机元素`, () => {
    let obj = new RandomizedSet();
    test("insert(1)", () => {
        expect(obj.insert(1)).toBe(true);
    });
    test("remove(2)", () => {
        expect(obj.remove(2)).toBe(false);
    });
    test("insert(2)", () => {
        expect(obj.insert(2)).toBe(true);
    });
    test("getRandom()", () => {
        const value = obj.getRandom();
        expect([1, 2].includes(value)).toBeTruthy();
    });
    test("remove(1)", () => {
        expect(obj.remove(1)).toBe(true);
    });
    test("insert(2)", () => {
        expect(obj.insert(2)).toBe(false);
    });
    test("getRandom()", () => {
        expect(obj.getRandom()).toBe(2);
    });
});