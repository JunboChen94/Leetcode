84. Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10

/////My solution
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int max = 0;
        int h, w;
        bool flag = true;
        for (int i = 0; i < heights.size(); i++) {
            h = heights[i];
            if (max < h) max = h;
            for (int j = i + 1; j < heights.size(); j++) {
                w = j - i + 1;
                if (h > heights[j]) h = heights[j];
                if (max < w * h) max = w * h;
            }
        }
        return max;
    }
};


///Better 
int largestRectangleArea(vector<int>& height) {
    height.push_back(0);
    const int size_h = height.size();
    stack<int> stk;
    int i = 0, max_a = 0;
    while (i < size_h) {
        if (stk.empty() || height[i] >= height[stk.top()]) stk.push(i++);
        else {
            int h = stk.top();
            stk.pop();
            max_a = max(max_a, height[h] * (stk.empty() ? i : i - stk.top() - 1));
        }
    }
    return max_a;
}

///Better

  class Solution {
    public:
        int largestRectangleArea(vector<int> &height) {
            
            int ret = 0;
            height.push_back(0);
            vector<int> index;
            
            for(int i = 0; i < height.size(); i++)
            {
                while(index.size() > 0 && height[index.back()] >= height[i])
                {
                    int h = height[index.back()];
                    index.pop_back();
                    
                    int sidx = index.size() > 0 ? index.back() : -1;
                    if(h * (i-sidx-1) > ret)
                        ret = h * (i-sidx-1);
                }
                index.push_back(i);
            }
            
            return ret;
        }
    };