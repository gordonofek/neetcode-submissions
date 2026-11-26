# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def hight (root: Optional[TreeNode]) -> int:
            nonlocal max_diameter
            if root == None:
                return 0
            else:
                left = hight(root.left)
                right = hight(root.right)

                if max_diameter < right+left:
                    max_diameter = right+left

                return max(left,right)+1
        
        hight(root)
        return max_diameter