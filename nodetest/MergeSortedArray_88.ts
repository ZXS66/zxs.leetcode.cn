
/** Do not return anything, modify nums1 in-place instead. */
export function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    const swap: number[] = [];
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
