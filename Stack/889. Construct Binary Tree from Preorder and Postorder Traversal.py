# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pri, poi = 0, 0
    def constructFromPrePost(self, pre, post):
        root = TreeNode(pre[self.pri])
        self.pri += 1
        if (root.val != post[self.poi]):
            root.left = self.constructFromPrePost(pre, post)
        if (root.val != post[self.poi]):
            root.right = self.constructFromPrePost(pre, post)
        self.poi += 1
        return root