//152. Maximum Product Subarray
//
//Given an integer array nums, find the contiguous subarray within an array(containing at least one number) which has the largest product.
//
//Example 1:
//
//Input: [2, 3, -2, 4]
//Output : 6
//Explanation : [2, 3] has the largest product 6.
//Example 2 :
//
//Input : [-2, 0, -1]
//Output : 0
//Explanation : The result cannot be 2, because[-2, -1] is not a subarray.

/////////My solution
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int old_pro = 0;
        int pro = 1;
        vector<int> check;
        for (int i = 0; i < nums.size(); i++) {
            pro *= nums[i];
            if (pro < 0) {
                if (i == nums.size()) {
                    check.push_back(old_pro);
                }
                if (nums[i + 1] < 0) continue;
                else {
                    check.push_back(old_pro);
                    pro = 1;
                    old_pro = 0;
                    continue;
                }
            }
            old_pro = pro;
        }
        int max = 0;
        for (int j = 0; j < check.size(); j++) {
            if (check[j] > max) max = check[j];
        }
        return max;
    }
};


///////// Better solution

#include<algorithm>

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.size() == 0) return 0;

        int result = nums[0];

        for (int i = 0; i < nums.size(); i++) {
            int accu = 1;
            for (int j = i; j < nums.size(); j++) {
                accu *= nums[j];
                result = max(result, accu);  // compare every possible solution
            }
        }

        return result;
    }
};