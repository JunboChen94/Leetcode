// devide and conquer using helper function left right and mid as arguments



class Solution {
    public int maxSubArray(int[] nums) {
        int len = nums.length;
        if (len == 1) return nums[0];
        return helper(nums, 0, len - 1);
    }
    public int helper(int[] nums, int left, int right) {
        if (left == right) return nums[left];
        int p = (left + right) / 2;
        int leftMax = helper(nums, left, p);
        int rightMax = helper(nums, p+1, right);
        int crossMax = crossSum(nums, left, right, p);
        return Math.max(leftMax, Math.max(rightMax, crossMax));
    }
    public int crossSum(int[] nums, int left, int right,int p) {
        if (left == right) return nums[left];
        
        int leftsum = Integer.MIN_VALUE;
        int cursum = 0;
        for (int i = p; i > left -1; --i) {
            cursum += nums[i];
            leftsum = Math.max(cursum, leftsum);
        }
        int rightsum = Integer.MIN_VALUE;
        cursum = 0;
        for (int i = p+1; i < right + 1; ++i) {
            cursum += nums[i];
            rightsum = Math.max(cursum, rightsum);
        }
        return leftsum + rightsum;
        
        
        
    }
}