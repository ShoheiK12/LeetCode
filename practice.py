# Level: easy

# 66 Plus one
"""
How to solve?
1. If the last digit is not 9, +1 to the last digit.
2. If a digit is 9, 9 will be 0 (9+1=10) and carry over(go to the next digit).
3. If all digits are 9, extra 1 at the front of 0s (999 → 1000).
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # range(start, stop, step) -> len(digits)-1: start with the last index, -1: stop at -1 (loop to 0), -1: move from right to left
        for i in range(len(digits)-1, -1,-1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                
        return [1] + digits

# 69. Sqrt(x)
"""
How to solve?
1. Use binary search -> square root is ascending order(= already sorted). 
2. Set up min, max, and midpoint.
3. Implement while loop until finding the answer.

Runtime is O(log n).
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # x = 0 or 1, square root is x itself.
        if x < 2:
            return x
        # set up left and right for binary search
        # left = 2 (minimum), right x //2 (maximum)
        # why not right = 2? The larger x becomes, the further the square root falls below 
        # half of x. Consequently, checking any range greater than x/2 is a waste of time.
        left, right = 2, x // 2
        
        # binart search
        while left <= right:
            # set up midpoint -> (left + right) // 2 is also OK.
            # In case x and y is very big number, left + (right - left) // 2 is preferred.
            mid = left + (right - left) // 2
            # set up num for checking if num is square root or not.
            num = mid * mid
            
            # if num = x, num is square root.
            if num == x:
                return mid
            # if num < x, search the right side (the larger range)
            elif num < x:
                left = mid + 1
            # if num > x, search the left side (the smaller range)
            else:
                right = mid - 1
        # When the loop finishes, right will be the largest integer that does not exceed x.
        return right
        
# 70. Climbing Stairs
"""
How to solve?
1. Fibonacci sequence
-> The number of ways to n = the number of way to n-1 + the numner of way to n+1 
-> Add the previous two to get the current number = Fibonacci sequence
2. if n = 1 or 2, return n.
3. Set up variables for fibonacci sequence
-> prev2 = 1 way to n-2. prev1 = 2 ways to n-1.
-> Ex: n = 3. prev2(n-2) is 1st-stair, so only 1 way to 1st-stair.
       prev1(n-1) is 2nd-stair, so 2 ways("1 step and 1 step" or "2 steps") to 2nd-stair.
4. Calculate from 3td-stair to the goal
-> current = prev1 + prev2 (Fibonacci sequence)
-> renew prev2 and prev1. For next step, prev1 = current, prev2 = prev1.

Runtime is O(n) because of one for-loop depending on n.
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Return n if n = 1 or 2
        if n <= 2:
            return n
        
        # Fibonacci sequence
        # prev2: n-2, prev1: n-1
        prev2 = 1
        prev1 = 2
        
        # Calculate from 3td-stair to the goal
        for i in range(3, n + 1):
            current = prev1 + prev2
            # Renew variables for nex calculation
            prev2 = prev1
            prev1 = current    
        # Return prev1 because prev1 = current
        return prev1

# 83. Remove Duplicates from Sorted List
"""
How to solve?
1. Set up pointer
2. Loop by the end of list
-> We need to check current and current.next
-> Because if we don't check current.next (only while current), it will cause an error when checking the last node. 

Runtime is O(n).
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # If list is empty or only one element in the list, return head
        if not head:
            return head
        # Set up pointer, as "current"
        current = head

        # Loop until the end of list
        while current and current.next:
            # If current value = next value of current, skip the next -> current.next = current.next.next
            if current.val == current.next.val:
                current.next = current.next.next
            # If the values are different, move pointer(current)
            else:
                current = current.next
        
        return head

# 88. Merge Sorted Array
# Answer 1
"""
How to solve?
1. Merge nums1 (only the first m elements) and nums2, and then sort it.
2. The final sorted array must be stored inside nums1.
-> We copy each element from 'merged' back into 'nums1' to satisfy the in-place requirement.

Runtime is O(n log n).
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Merge nums1 and nums2,and then sort it.
        merged = sorted(nums1[:m] + nums2)
    
        # The final sorted array
        for i in range(m + n):
            nums1[i] = merged[i]

# Answer 2
"""
How to solve?
1. Put elements backward in nums1
-> If we put elements forward in nums1, the original elements in nums1 will be updated.
-> It means that we need to copy original nums1 to avoid this update.
-> But, If putting elements backward, we don't care about update. 
=> Line them up from biggest to smallest, starting from the back.
2. Set ip three pointers for the last element nums1, nums2, and the last position of nums1.
-> Why setting up them for the last elements? Because this list is ascending order.
3. Compare the element of p1 and the element of p2. 
-> Put bigger element in the end of nums1 (= p).

Runtime is O(n).
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Set up tree pinters
        p1 = m - 1      # the end of num1 without 0s.
        p2 = n - 1      # the end of num2.
        p = m + n - 1   # the end of original nums1 = num1 with 0s.

        # Loop if p1 and p2 >= 0. 
        while p1 >= 0 and p2 >= 0:
            # If nums1 > nums2, put nums1[p1] in the end of priginal nums1
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                # Put next number after p1.
                p1 -= 1
            # If nums2 > nums1, put nums2[p2] in the end of priginal nums1
            else:
                nums1[p] = nums2[p2]
                # Put next number after p2.
                p2 -= 1
            p -= 1

        # In case elements still remians in nums2 and nums1 finish first.
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

# 94. Binary Tree Inorder Traversal
"""
How to solve?
1. To perform an Inorder Traversal, we visit the nodes in a specific order: Left → Root → Right.
2. Use recursion.
-> A tree is a recursive data structure. Recursion naturally mimics this structure by applying the same logic to each subtree.

Runtime is O(n).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # Make an empty list to store the result.
        result = []

        # Visit node recursively
        def helper(node):
            if not node:
                return

            # Search left node first
            helper(node.left)

            # Append the value if cannot moving any further to the left
            result.append(node.val)

            # Search right node
            helper(node.right)
            
        helper(root)
        
        return result

# 100. Same Tree
"""
How to solve?
1. We need to check both nodes are same.
-> If both of nodes are None, it means same.
-> If either node is None or has diffrent values,  not same.
2. When both nodes are not None and have same values, check each left node and each right node recursively.
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
