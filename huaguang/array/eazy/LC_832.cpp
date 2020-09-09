#include <vector>
//Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
//
//To flip an image horizontally means that each row of the image is reversed.For example, flipping[1, 1, 0] horizontally results in[0, 1, 1].
//
//To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting[0, 1, 1] results in[1, 0, 0].


// my solution 
class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        if (A.empty()) return A;
        int rows = A.size();
        int clo = A[0].size();
        for (int i = 0; i < rows; i++) {
            int j = 0, k = clo - 1;
            while (j <= k) {         
                swap(A[i][j], A[i][k]);
                A[i][j] ^= 1;
                A[i][k] ^= 1;
                if (j == k) A[i][j] ^= 1;
                j++;
                k--;
            }
        }
        return A;
    }
};

// better solution
// class Solution {
// public:
//     vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
//         if(A.empty()) return A;
//         for(auto& row : A){
//             std::reverse(std::begin(row), std::end(row));
//             std::for_each(row.begin(), row.end(), [](int& item){ item ^= 1; });
//             }  
//         return A;
//     }
// };


//************************lambda 表达式********************************
// [capture list] (params list) mutable exception-> return type { function body }
// sort(lbvec.begin(), lbvec.end(), [](int a, int b) -> bool { return a < b; });   // Lambda表达式