#include <iostream>
using namespace std;

struct TreeNode {
    
    int data;
    TreeNode *left, *right;
    
    TreeNode(int val) {
        
        data = val;
        left = nullptr;
        right = nullptr;
    }
};

TreeNode* constructTreeFromArray(int nums[], int start, int end) {
    
    if (start > end) {
        
        return nullptr;
    }
    
    int mid = start + (end - start) / 2;
    TreeNode* node = new TreeNode(nums[mid]);
    
    node->left = constructTreeFromArray(nums, start, mid - 1);
    node->right = constructTreeFromArray(nums, mid + 1, end);
    
    return node;
}

TreeNode* sortedArrayToBST(int nums[], int size) {

    if (size == 0) {

        return nullptr;
    }

    return constructTreeFromArray(nums, 0, size - 1);
}