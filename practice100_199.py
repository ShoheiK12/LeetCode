# Level: Easy

# 100. Same Tree
"""
How to solve?
1. We need to check both nodes are same.
-> If both of nodes are None, it means same.
-> If either node is None or has diffrent values,  not same.
2. When both nodes are not None and have same values, check each left node and each right node recursively.

Runtime is O(n).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # 1. If both of nodes are None, return True.
        if not p and not q:
            return True
        
        # 2. If either node is None or has different values, return False
        if not p or not q or p.val != q.val:
            return False
        
        # 3. When both nodes are not None and have same values, check left and right recursively. 
        # If both of conditions are True, return True.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# 101. Symmentric Tree
"""
How to solve?
1. check whether it is a mirror of itself.
= check outside of whole tree (left of left subtree = right of right subtree) and inside og whole tree (left of right subtree = right of left subtree).

Runtime is O(n).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # if no nodes in whole tree, it means symmetric.
        if not root:
            return True
        
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        # 1. If both of left and right subtrees are empty, it means symmetric.
        if not left and not right:
            return True
        
        # 2. If either left or right subtree is empty, or the values are different, it means not symmetric.
        if not left or not right or left.val != right.val:
            return False
        
        # 3. Otherwise, check left and right tree recursively
        # left of left subtree = right of right subtree
        # and left of right subtree = right of left subtree
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

# 104. Maximum Depth of Binary Tree
"""
How to solve?
1. Calculate the depth of the left subtree and the right subtree respectively, 
then add 1 (for the current level) to the greater of the two.

Runtime is O(n).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # 1. If nodes are empty, return 0.
        if not root:
            return 0
        
        # 2. See the max depth of left subtrees.
        left_depth = self.maxDepth(root.left)
        
        # 3. See the max depth of right subtrees.
        right_depth = self.maxDepth(root.right)
        
        # 4.  Add one (parent nodes) to the maximum depth of the left and right subtrees.
        return max(left_depth, right_depth) + 1

# 108. Convert Sorted Array to Binary Search Tree
"""
How to solve?
1. The rule for BST is that values to the left must be smaller than the parent, and values to the right must be larger than the parent.
-> Since the array(list) is already sorted in ascending order, choosing the middle value as the parent results in:
The smaller numbers are on the left, and the larger numbers are on the right. Those are divided exactly in half.
2. Divide the array(list) into left, midpoint and right.
-> The midpoint nums[len(nums)//2] must be the root node of nums, becuase nums is a sorted list.
3. Create the TreeNode using the midpoint value.
4. Recursion. 
Pass the left half of the list to sortedArrayToBST to build the left subtree. Do the same for the right half of the list to build the right subtree.
5. Connect the returned left subtrees and right subtrees to the current node (root.left, root.right).

Runtime is O(n).
Space complexity is O(log n).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        # 1. If the list is empty, return None.
        if not nums:
            return None
        
        # 2. Find midpoint index of the list.
        mid = len(nums) // 2
        
        # 3. Create a parent node using midpoint value.
        root = TreeNode(nums[mid])
        
        # 4. Create left subtrees recursively using left elements from the midpoint.
        root.left = self.sortedArrayToBST(nums[:mid])
        
        # 5. Create right subtrees recursively using right elements from the midpoint.
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        # 6. Return the whole tree
        return root

# 110. Balanced Binary Tree
"""
How to solve?
1. Height-balanced tree means the height difference between the left and right subtrees is at most 1 for every node.
2. If balanced, return the height. If unbalanced, return -1.
3. Get the height of left and right subtrees. 
-> If the subtree is unbalanced, return -1. 
4. If both subtrees are balanced, calculate the remainder of the height of both left and right subtrees.

Runtime is O(n).
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.checkHeight(root) != -1

    def checkHeight(self, node):
        # 1. If node is empty, the height is 0.
        if not node:
            return 0
        
        # 2. Get the height of left subtree
        left_h = self.checkHeight(node.left)
        if left_h == -1: return -1  # If find unbalance in left subtree, then -1.
        
        # 3. Get the height of right subtree
        right_h = self.checkHeight(node.right)
        if right_h == -1: return -1 # If find unbalance in left subtree, then -1.
        
        # 4. Check if the whole tree is unbalance or not.
        # If the remainder is greater than 1, return -1 = unbalanced
        if abs(left_h - right_h) > 1:
            return -1
            
# 111. Minimum depth of Binary Tree
"""
How to solve?
1. This question asks the number of nodes.
-> Ex: 3(parent)->9(left child)&20(right child) -> The min depth is 2.
2. Use recursion.
3. (When nodes have both left and right children)The min depth is 1 (current node) + min(self.minDepth(root.left),self.minDepth(root.right))
4. (When nodes have either left or right children(one side is empty)) 3 equation does not suit this case.
-> Ex: 3(parent)->empty(left child)&20(right child) -> If use this equation, 1 + min(0,1) = 1 + 0 = 1. But, the answer is 2 because there are 2 nodes.
5. In case 4, the min depth means the number of nodes that exist in this tree. 
-> So, if either side is empty, this empty side should be ignored = Check the only node that exists in the tree in case of empty nodes.

Runtime is O(n).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        if not root.left:
            return 1 + self.minDepth(root.right)

        if not root.right:
            return 1 + self.minDepth(root.left)
            
        return 1 + min(self.minDepth(root.left),
                       self.minDepth(root.right))

# 112. Path Sum
"""
How to solve?
1. Check the value of node one by one.
-> Use recursion.
2. If no tree (empty list), return false.
3. When reach to leaf node (root.left == None and root.right == None), check if root.val (leaf node) == tragetSum.
-> If root.val == tragetSum, return True. Otherwise return false.
4. When on the way to leaf node, go to targetSum -= root.val to reduce the sum.
5. Set up self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum) for next node (Recursion).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        targetSum -= root.val

        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum))
