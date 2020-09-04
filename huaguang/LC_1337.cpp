//1337. The K Weakest Rows in a Matrix
//
//Given a m* n matrix mat of ones(representing soldiers) and zeros(representing civilians), return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.
//
//A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they have the same number of soldiers but i is less than j.Soldiers are always stand in the frontier of a row, that is, always ones may appear firstand then zeros.
//
//
//
//Example 1:
//
//Input: mat =
//[[1, 1, 0, 0, 0],
//[1, 1, 1, 1, 0],
//[1, 0, 0, 0, 0],
//[1, 1, 0, 0, 0],
//[1, 1, 1, 1, 1]],
//k = 3
//Output: [2, 0, 3]
//Explanation :
//    The number of soldiers for each row is :
//row 0 -> 2
//row 1 -> 4
//row 2 -> 1
//row 3 -> 2
//row 4 -> 5
//Rows ordered from the weakest to the strongest are[2, 0, 3, 1, 4]


class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        if (k == 0 || mat.empty()) return {};
        int n = mat[0].size() - 1;
        vector<int> res;
        for (int i = 0; i < mat.size(); i++) {
            for (int j = 1; j < mat[0].size(); j++) {
                mat[i][0] += mat[i][j];
            }
            mat[i][n] = i;
        }
        sort(mat.begin(), mat.end(), [](const vector<int>& a, const vector<int>& b) {
            return (a[0] != b[0]) ? a[0] < b[0] : a[a.size() - 1] < b[b.size() - 1];
            });
        for (int l = 0; l < k; l++) {
            res.push_back(mat[l][n]);
        }
        return res;
    }
};·