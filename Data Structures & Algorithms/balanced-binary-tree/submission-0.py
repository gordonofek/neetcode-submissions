# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def hight (root: Optional[TreeNode]) -> int:
            nonlocal is_balanced
            if root == None:
                return 0
            else:
                left = hight(root.left)
                right = hight(root.right)

                if abs(left-right)>1:
                    is_balanced = False

                return max(left,right)+1
        
        hight(root)
        return is_balanced
        