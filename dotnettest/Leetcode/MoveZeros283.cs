// https://leetcode.cn/problems/move-zeroes/?envType=study-plan-v2&envId=top-100-liked

public class MoveZeros283
{
    public void MoveZeroes(int[] nums)
    {
        if (nums.Length <= 1)
        {
            // no moves needed
            return;
        }
        int idxOfZero = 0, idxOfNonZero = 0;
        int n = nums.Length;
        while (idxOfZero < n)
        {
            if (nums[idxOfZero] != 0)
            {
                // swap
                int temp = nums[idxOfZero];
                nums[idxOfZero] = nums[idxOfNonZero];
                nums[idxOfNonZero] = temp;
                idxOfNonZero++;
            }
            idxOfZero++;
        }
    }
}