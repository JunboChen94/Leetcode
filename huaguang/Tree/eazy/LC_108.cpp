//108. Convert Sorted Array to Binary Search Tree
//
//Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
//For this problem, a height - balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
//
//Example:
//
//Given the sorted array : [-10, -3, 0, 5, 9] ,
//One possible answer is : [0, -3, 9, -10, null, 5] , which represents the following height balanced BST :
//
//0
/// \
//- 3   9
///   /
//-10  5

///// Solution
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if (nums.size() == 0) return NULL;

        int mid = nums.size() / 2;
        TreeNode* newNode = new TreeNode(nums[mid]);

        if (mid - 1 >= 0) {
            vector<int> left(nums.begin(), nums.begin() + mid);
            newNode->left = sortedArrayToBST(left);
        }

        if (mid + 1 < nums.size()) {
            vector<int> right(nums.begin() + mid + 1, nums.end());
            newNode->right = sortedArrayToBST(right);
        }

        return newNode;

    }
};