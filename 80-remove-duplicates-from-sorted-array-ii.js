/**
 * @param {number[]} nums asc numbers
 * @return {number}
 */
var removeDuplicates = function (nums) {
    let idx = 0;
    let occurs = 0;
    let lastValue = undefined;
    while (nums[idx] !== undefined) {
        if (nums[idx] === lastValue) {
            occurs++;
            if (occurs > 2) {
                nums.splice(idx, 1);
                idx--;
            }
        } else {
            occurs = 1;
            lastValue = nums[idx];
        }
        idx++;
    }
    return nums.length;
};

const testcases = [
    { nums: [1, 1, 1, 2, 2, 3], k: 5 },
    { nums: [0, 0, 1, 1, 1, 1, 2, 3, 3], k: 7 },
    { nums: [1, 1, 1], k: 2 },
];

testcases.forEach(testcase => {
    console.log(`input: ${testcase.nums}`);
    console.log(`output: ${removeDuplicates(testcase.nums)} (should equals to ${testcase.k})`);
    console.log(`after action: ${testcase.nums}`);
    console.log('-------------------------');
})