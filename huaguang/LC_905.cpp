//905. Sort Array By Parity
//
//Given an array A of non - negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
//
//You may return any answer array that satisfies this condition.


// my solution 
class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        vector<int> result;
        for (int i = 0; i < A.size(); i++) {
            if (A[i] % 2 == 0) {
                result.push_back(A[i]);
            }
        }
        for (int j = 0; j < A.size(); j++) {
            if (A[j] % 2 == 1) {
                result.push_back(A[j]);
            }
        }
        return result;
    }
};

// better solution

class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        int i = 0;
        for (int j = 0; j < A.size(); ++j) {
            if (A[j] % 2 == 0) {
                swap(A[i], A[j]);
                i++;
            }
        }
        return A;
    }
};
