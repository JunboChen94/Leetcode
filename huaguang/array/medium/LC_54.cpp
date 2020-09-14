//54. Spiral Matrix
//
//Given a matrix of m x n elements(m rows, n columns), return all elements of the matrix in spiral order.
//
//Example 1:
//
//Input:
//[
//    [ 1, 2, 3 ],
//    [4, 5, 6],
//    [7, 8, 9]
//]
//Output : [1, 2, 3, 6, 9, 8, 7, 4, 5]
//Example 2 :
//
//    Input :
//    [
//        [1, 2, 3, 4],
//        [5, 6, 7, 8],
//        [9, 10, 11, 12]
//    ]
//Output : [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

#include<iostream>
#include<vector>

using namespace std;
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int row_beg = 0;
        int row_end = matrix.size();
        int clm_beg = 0;
        int clm_end = matrix[0].size();
        vector<int> res;
        while (true) {  //row_beg < row_end && clm_beg < clm_end
            for (int i = clm_beg; i < clm_end; i++) {
                res.push_back(matrix[row_beg][i]);
            }
            row_beg++;
            if (row_beg == row_end) break;
            for (int j = row_beg; j < row_end; j++) {
                res.push_back(matrix[j][clm_end - 1]);
            }
            clm_end--;
            if (clm_beg == clm_end) break;
            for (int k = clm_end - 1; k >= clm_beg; k--) {
                res.push_back(matrix[row_end - 1][k]);
            }
            row_end--;
            if (clm_beg == clm_end) break;
            for (int l = row_end - 1; l >= row_beg; l--) {
                res.push_back(matrix[l][clm_beg]);
            }
            clm_beg++;
            if (row_beg == row_end) break;
        }
        return res;
    }
};

int main() {
    vector<vector<int>> test = { {1, 2, 3, 4 }, {5, 6, 7, 8},{9,10,11,12} };
    Solution so;

    vector<int> result;
    result = so.spiralOrder(test);

    for (int p = 0; p < result.size(); p++) {
        cout << result[p] << ", ";
    }
}

///// Better solution
//class Solution {
//public:
//    vector<int> spiralOrder(vector<vector<int>>& matrix) {
//        vector<int>ans;
//        if (matrix.size() == 0)
//            return ans;
//        int top = 0;
//        int bottom = matrix.size() - 1;
//        int left = 0;
//        int right = matrix[0].size() - 1;
//        int size = matrix.size() * matrix[0].size();
//        while (ans.size() < size) {
//            for (int i = left; i <= right && ans.size() < size; i++)
//                ans.push_back(matrix[top][i]);
//            top++;
//            for (int i = top; i <= bottom && ans.size() < size; i++)
//                ans.push_back(matrix[i][right]);
//            right--;
//            for (int i = right; i >= left && ans.size() < size; i--)
//                ans.push_back(matrix[bottom][i]);
//            bottom--;
//            for (int i = bottom; i >= top && ans.size() < size; i--)
//                ans.push_back(matrix[i][left]);
//            left++;
//
//        }
//        return ans;
//    }
//};