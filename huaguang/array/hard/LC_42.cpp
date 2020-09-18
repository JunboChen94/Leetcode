//42. Trapping Rain Water
//
//Given n non - negative integers representing an elevation map where the width of each bar is 1, 
//compute how much water it is able to trap after raining.
//
//
//The above elevation map is represented by array[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1].In this case, 
//6 units of rain water(blue section) are being trapped.Thanks Marcos for contributing this image!
//
//Example:
//
//Input: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
//Output : 6


/////Solution

class Solution {
public:
    int trap(vector<int>& height) {
        const int n = height.size();
        int ans = 0;
        vector<int> l(n);  // need create vector l(n)! not only l
        vector<int> r(n);
        for (int i = 0; i < n; i++) {     // find left max
            l[i] = i == 0 ? height[i] : max(height[i], l[i - 1]);
        }
        for (int i = n - 1; i >= 0; i--) {  // find right max
            r[i] = i == n - 1 ? height[i] : max(height[i], r[i + 1]);
        }
        for (int i = 0; i < n; i++) {  // the rain on i should be min(left,right) - height[i]
            ans += min(l[i], r[i]) - height[i];
            // don't need to judge the boundary cuz before already include i itself if (min(l[i], r[i]) > height[i]) 
        }
        return ans;
    }
};