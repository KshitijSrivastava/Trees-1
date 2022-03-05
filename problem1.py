

# https://leetcode.com/problems/validate-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid_recur(root, minimum, maximum):
            if root is None:                        #if root is None return True
                return True
            
            if root.val <= minimum or root.val >= maximum:  
                #if root.val is less than minimum or greater than or equal to maximum, not valid
                return False
            
            #traverse the lft and right tree
            return isValid_recur(root.left, minimum, root.val) and isValid_recur(root.right, root.val, maximum)
        
        return isValid_recur(root, float('-inf'), float('inf'))
            