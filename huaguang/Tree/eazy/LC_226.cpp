//226. Invert Binary Tree
//
//Invert a binary tree.
//
//Example:
//Input:
//4
/// \
//2     7
/// \ / \
//1   3 6   9
//
//Output:
//4
/// \
//7     2
/// \ / \
//9   6 3   1


////Solution 
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr) return NULL;
        swap(root->left, root->right);
        invertTree(root->left);
        invertTree(root->right);
        return root;
    }
};