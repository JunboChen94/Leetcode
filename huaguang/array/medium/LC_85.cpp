//85. Maximal Rectangle
//
//Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
//
//Input: matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
//Output : 6
//Explanation : The maximal rectangle is shown in the above picture.
//Example 2 :
//
//	Input : matrix = []
//	Output : 0
//	Example 3 :
//
//	Input : matrix = [["0"]]
//	Output : 0
//	Example 4 :
//
//	Input : matrix = [["1"]]
//	Output : 1
//	Example 5 :
//
//	Input : matrix = [["0", "0"]]
//	Output : 0
//


///// Solution

class Solution {
public:
    int maximalRectangle(vector<vector<char> >& matrix) {
        if (matrix.empty()) {
            return 0;
        }
        int maxRec = 0;
        vector<int> height(matrix[0].size(), 0);
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                if (matrix[i][j] == '0') {
                    height[j] = 0;
                }
                else {
                    height[j]++;
                }
            }
            maxRec = max(maxRec, largestRectangleArea(height));
        }
        return maxRec;
    }

    int largestRectangleArea(vector<int>& height) {
        stack<int> s;
        height.push_back(0);
        int maxSize = 0;
        for (int i = 0; i < height.size(); i++) {
            if (s.empty() || height[i] >= height[s.top()]) {
                s.push(i);
            }
            else {
                int temp = height[s.top()];
                s.pop();
                maxSize = max(maxSize, temp * (s.empty() ? i : i - 1 - s.top()));
                i--;
            }
        }
        return maxSize;
    }
};