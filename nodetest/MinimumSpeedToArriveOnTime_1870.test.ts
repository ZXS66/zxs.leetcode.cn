// https://leetcode.cn/problems/minimum-speed-to-arrive-on-time/description/

function minSpeedOnTime(dist: number[], hour: number): number {
    if (dist.length > Math.ceil(hour)) {
        return -1;
    }
    let minSpeed = Math.floor(dist.reduce((acc, cur) => acc + cur, 0) / hour);
    let maxSpeed = 10_000_000;
    // can be optimized by avoiding function calls
    const getArriveTime = (dist: number[], speed: number): number => {
        const n = dist.length;
        let arriveTime = 0;
        dist.forEach((v, i) => {
            if (i === (n - 1)) {
                arriveTime += v / speed;
            } else {
                arriveTime += Math.ceil(v / speed);
            }
        })
        return arriveTime;
    };
    while(minSpeed<maxSpeed){
        const midSpeed = Math.floor((minSpeed + maxSpeed) / 2);
        const arriveTime = getArriveTime(dist, midSpeed);
        if (arriveTime > hour) {
            minSpeed = midSpeed + 1;
        } else {
            maxSpeed = midSpeed;
        }
    }
    return minSpeed;
};

// unit test
import { describe, expect, test } from '@jest/globals';
const testcases = [
    { dist: [1, 3, 2], hour: 6, result: 1 },
    { dist: [1, 3, 2], hour: 2.7, result: 3 },
    { dist: [1, 3, 2], hour: 1.9, result: -1 },
];

describe.each(testcases)(`dist: $dist, hour: $hour`, ({ dist, hour, result }) => {
    test(`returns ${result}`, () => {
        expect(minSpeedOnTime(dist, hour)).toBe(result);
    });
});

