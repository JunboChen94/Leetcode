//938. Range Sum of BST
//
//Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R(inclusive).
//The binary search tree is guaranteed to have unique values.
//
//Example 1:
//Input: root = [10, 5, 15, 3, 7, null, 18], L = 7, R = 15
//Output : 32
//
//Example 2 :
//Input : root = [10, 5, 15, 3, 7, 13, 18, 1, null, 6], L = 6, R = 10
//Output : 23
//
//Note :
//The number of nodes in the tree is at most 10000.
//The final answer is guaranteed to be less than 2 ^ 31.



////Solution 

class Solution {  
public:
    int rangeSumBST(TreeNode* root, int L, int R, int sum = 0) {
        if (root == nullptr) return 0;
        sum += (root->val >= L && root->val <= R) ? root->val : 0;   // recursive and sum the left and right value
        sum += rangeSumBST(root->left, L, R);
        sum += rangeSumBST(root->right, L, R);
        return sum;

    }
};



//// Other solution

/// 1 - liner solution : same idea as above, but written as one line of code
class Solution {
public:
    int rangeSumBST(TreeNode* root, int L, int R) {
        return root ? rangeSumBST(root->left, L, R)
            + rangeSumBST(root->right, L, R)
            + (L <= root->val && root->val <= R ? root->val : 0) : 0;
    }
};


/// Contest solution : Same idea as above, but this is the solution which I came up with during this contest.I personally prefer using go() for recursive function nomenclature...
class Solution {
    int go(TreeNode* root, const int L, const int R, int sum = 0) {
        if (root->left) sum += go(root->left, L, R);
        sum += (L <= root->val && root->val <= R) ? root->val : 0;
        if (root->right) sum += go(root->right, L, R);
        return sum;
    }
public:
    int rangeSumBST(TreeNode* root, int L, int R) {
        return root ? go(root, L, R) : 0;
    }
};