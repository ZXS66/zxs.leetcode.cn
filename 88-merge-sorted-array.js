/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (nums1, m, nums2, n) {
    const swap = [];
    while (m > 0 || n > 0) {
        if (m > 0 && n > 0) {
            if (nums1[m - 1] > nums2[n - 1]) {
                swap.push(nums1[m - 1]);
                m--;
            } else {
                swap.push(nums2[n - 1]);
                n--;
            }
        } else if (m > 0) {
            swap.push(nums1[m - 1]);
            m--;
        } else {
            swap.push(nums2[n - 1]);
            n--;
        }
    }
    for (let i = 0; i < swap.length; i++) {
        nums1[i] = swap[swap.length - i - 1];
    }
};


const testcases = [
    {
        nums1: [1, 2, 3, 0, 0, 0],
        m: 3,
        nums2: [2, 5, 6],
        n: 3
    },
    {
        nums1: [1],
        m: 1,
        nums2: [],
        n: 0
    },
    {
        nums1: [0],
        m: 0,
        nums2: [1],
        n: 1
    },
];

for (let i = 0; i < testcases.length; i++) {
    const testcase = testcases[i];
    merge(testcase.nums1, testcase.m, testcase.nums2, testcase.n);
    console.log(testcase.nums1);
}
