//128. Longest Consecutive Sequence
//
//Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
//
//Your algorithm should run in O(n) complexity.
//
//Example:
//
//Input: [100, 4, 200, 1, 3, 2]
//Output : 4
//Explanation : The longest consecutive elements sequence is[1, 2, 3, 4].Therefore its length is 4.
//


#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


////My Solution

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int length = 0;
        int temp = 1;
        vector<int> t;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            if (i == nums.size() - 1) break;
            if (nums[i + 1] == nums[i] + 1) temp++;
            else if (nums[i + 1] != nums[i] + 1) {
                t.push_back(temp);
                temp = 1;
            }
        }
        for (int j = 0; j < t.size(); j++) {
            if (length < t[j]) length = t[j];
        }
        return length;
    }
};



//// Better Solution

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> h(nums.begin(), nums.end());
        int ans = 0;
        for (num : nums) {
            if (!h.count(num - 1)) {  // check whether item has left side value. if not start a new sequence
                int l = 0;
                while (h.count(num++)) l++;  // if it has, count ++
                ans = max(ans, l);  // check longest
            }
        }
        return ans;
    }
};