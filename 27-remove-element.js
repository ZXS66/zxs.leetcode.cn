/**
 * @param {number[]} nums data array
 * @param {number} val value to be removed
 * @return {number} return value
 */
function removeElement(nums, val) {
    let len = nums.length;
    let k = 0;
    for (let i = 0; i < len; i++) {
        if (nums[i] === val) {
            nums[i] = 0;
        } else {
            k++;
        }
    }
    nums.sort((a, b) => b - a);
    return k;
};

// test cases

let nums = [0,1,2,2,3,0,4,2];
const val = 2; // 要移除的值
let expectedNums = []; // 长度正确的预期答案。
// 它以不等于 val 的值排序。

let k = removeElement(nums, val); // 调用你的实现

console.log(k === 2)