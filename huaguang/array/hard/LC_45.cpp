//45. Jump Game II
//
//Given an array of non - negative integers, you are initially positioned at the first index of the array.
//
//Each element in the array represents your maximum jump length at that position.
//
//Your goal is to reach the last index in the minimum number of jumps.
//
//Example:
//
//Input: [2, 3, 1, 1, 4]
//Output : 2
//Explanation : The minimum number of jumps to reach the last index is 2.
//Jump 1 step from index 0 to 1, then 3 steps to the last index.
//Note :
//
//You can assume that you can always reach the last index.


class Solution {
public:
    int jump(vector<int>& nums) {
        int jump = 0;
        int curr = 0;   // before this step the maxmum reach
        int maxstep = 0;   // with this step maxmum reach
        for (int i = 0; i < nums.size() - 1; i++) {
            if (i + nums[i] > maxstep) maxstep = i + nums[i]; // find the maxmum step
            if (i == curr) {    // if i == cur update the curr, which means u definate need to jump once
                jump++;   
                curr = maxstep;
            }
        }
        return jump;  // after the loop return the jump. cuz i < nums.size() - 1, return the mim jump that we can reach to last value
    }
};