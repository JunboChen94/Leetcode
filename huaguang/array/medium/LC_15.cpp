//15. 3Sum
//
//Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0 ? Find all unique triplets in the array which gives the sum of zero.
//
//Notice that the solution set must not contain duplicate triplets.
//
//
//
//Example 1:
//
//Input: nums = [-1, 0, 1, 2, -1, -4]
//Output : [[-1, -1, 2], [-1, 0, 1]]
//Example 2 :
//
//    Input : nums = []
//    Output : []
//    Example 3 :
//
//    Input : nums = [0]
//    Output : []

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        if (n < 3) return{};
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        for (int i = 0; i < n && nums[i] <= 0; i++) {
            if (i == 0 || nums[i - 1] != nums[i]) threesum2(i, n, nums, res);
        }
        return res;
    }
    void threesum2(int i, int n, vector<int>& nums, vector<vector<int>>& res) {
        int j = i + 1, k = n - 1;
        while (j < k) {
            int sum = nums[i] + nums[j] + nums[k];
            if (sum < 0) j++;
            else if (sum > 0) k--;
            else {
                res.push_back({ nums[i],nums[j],nums[k] });
                j++;
                while (j < k && nums[j] == nums[j - 1]) j++;
            }
        }
    }
};

// use two pointer, sum < 0 j++ ; sum > 0 k--