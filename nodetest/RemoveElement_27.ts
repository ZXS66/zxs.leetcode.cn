export function removeElement(nums: number[], val: number): number {
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
