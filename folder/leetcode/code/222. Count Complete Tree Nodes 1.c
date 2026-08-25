#include <stddef.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int countNodes(struct TreeNode* root) {
    if (root == NULL) {
        return 0;
    }
    int leftHeight = 0;
    int rightHeight = 0;
    struct TreeNode* leftNode = root;
    struct TreeNode* rightNode = root;
    while (leftNode != NULL) {
        leftHeight++;
        leftNode = leftNode->left;
    }
    while (rightNode != NULL) {
        rightHeight++;
        rightNode = rightNode->right;
    }
    if (leftHeight == rightHeight) {
        return (1 << leftHeight) - 1;
    }
    return 1 + countNodes(root->left) + countNodes(root->right);
}
