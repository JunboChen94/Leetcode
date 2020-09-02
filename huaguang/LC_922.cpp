//922. Sort Array By Parity II
//
//Given an array A of non - negative integers, half of the integers in A are odd, and half of the integers are even.
//
//Sort the array so that whenever A[i] is odd, i is odd;and whenever A[i] is even, i is even.
//
//You may return any answer array that satisfies this condition.



class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& A) {
        vector<int> result(A.size());
        int x = 0;
        int y = 1;
        for (int i = 0; i < A.size(); i++) {
            if (A[i] % 2) {
                result[y] = A[i];
                y += 2;
            }
            else {
                result[x] = A[i];
                x += 2;
            }
        }
        return result;
    }
};


// class Solution {
// public:
//     vector<int> sortArrayByParityII(vector<int>& A) {
//         int i = 0;
//         for(int j = 0;j<A.size();j++){
//             if(A[j]%2 ==0 ){
//                 swap(A[j],A[i]);
//                 i+=2;
//             }
//         }
//         return A;
//     }
// };