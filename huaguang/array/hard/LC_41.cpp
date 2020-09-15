41. First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1

Follow up:
Your algorithm should run in O(n) time and uses constant extra space.

/// swap every element to increase sequence and equal to index +1, then search from the first element, missing min integer
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        if (nums.size() == 0) return 1;
        int temp;
        for (int i = 0; i < nums.size(); i++) {
            while (nums[i] > 0 && nums[i] <= nums.size() && nums[nums[i] - 1] != nums[i]) {
               /* temp = nums[i];
                nums[i] = nums[nums[i] - 1];  
                nums[nums[i] - 1] = temp;*/  // in valid value, cuz num[i]=4 right now. nums has no (4+1)th element
                temp = nums[nums[i] - 1];        // first change nums[nums[i]-1] or the nums[i] gonna to change
                nums[nums[i] - 1] = nums[i];
                nums[i] = temp;
            }
        }
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != i + 1) return i + 1;
        }
    }
};