/**
 * @param {number[]} nums asc numbers
 * @return {number}
 */
var removeDuplicates = function (nums) {
    const maxDuplicates = 2;
    let i = 0;
    let dup = 1;
    for (let j = 1; j < nums.length; j++) {
        if (nums[i] !== nums[j]) {
            i++;
            nums[i] = nums[j];
            dup = 1;
        } else if (dup <= maxDuplicates) {
            nums[i] = nums[j];
            dup++;
        } else {
            i++;
            dup++;
        }
    }
    return i + 1;
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