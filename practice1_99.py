# Level: easy

# 1. Two Sum
"""
How to solve?
1. Use two for-loops to fix the first num and the second num.
2. Check if nums[1] + nums[j] == target.

Runtime is O(n^2).
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

# 9. Palindrome Number
"""
How to solve?
1. Covert x into string and put it in list.
2. Check palindrome comparing digits[i] != digits[-(i + 1)].

Runtime is O(n).
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        digits = list(str(x))

        for i in range(len(digits) // 2):
            if digits[i] != digits[-(i + 1)]:
                return False

        return True

# 13. Roman to Integer
"""
How to solve?
1. Make a dictionary to store Roman numbers and value.
2. Check string backwards (from right to left)
-> If we check string forwards (from left to right), we need to check i+1 (= need to check Index Out of Bounds).
-> If checking backwards, just check the next char, and if smaller, -1. Otherwise, +1. 

Runtime is O(n). Because we check string only once, so runtime depends on the length of string.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        # check string backwards so that we can calculate easily.
        for char in reversed(s):
            value = roman_dict[char]
            # if value < prev_value, substarct
            if value < prev_value:
                total -= value
            # if value > prev_value, add and renew prev_value
            else:
                total += value
                prev_value = value

        return total

# 14. Longest Common Prefix
"""
How to solve?
1. Set up loop time based on shotest string.
2. Check characters using index.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if strs are empty, return ""
        if not strs:
            return ""
        
        # set up shotest string in the strs based on length
        shortest_str = min(strs, key=len)
        
        for i in range(len(shortest_str)):
            # check if the prefix of shortest string is the same or not one by one
            for string in strs:
              # if prefix is not same, then return prefix to the same position.
                if string[i] != shortest_str[i]:
                    return shortest_str[:i]
        # if shortest string is prefilx, return this string.
        return shortest_str  

20. Valid Parentheses
"""
How to solve?
1. Prepare for empty stack
2. Prepare for bracket_map 
3. If char == ( or { or [, append char to stack.
4. if char == ) or } or ], go to else clause.
-> 4.1 If corresponding bracket is not in stack, return False.
-> 4.2 (When stack is not empty,) Pick up top of the stack = the last char in stack (LIFO).
-> 4.3 If different type of brancket, return False.
5. Return not stack = If stack is empty, return True. Otherwise, return False.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if bracket_map[char] != top:
                    return False

        return not stack

# 21. Merge Two Sorted Lists
"""
How to solve?
1. Initialize a dummy node
2. Compare and Link
3. Attach remainder

Runtime is O(n+m).
"""

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Make start-point for merged list
        dummy = ListNode(0)
        # Pointer for the tail of merged list
        current = dummy

        # Compare list1 value and list2 value
        # Add smaller value to merged list and move a pointer forward.
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next

# 26. Remove Duplicates from Sorted Array
"""
How to solve?
1. Check nums[j] is unique or not.
2. If unique,  nums[i] = nums[j] and return the number of unique elements in nums.

Runtime is O(n).
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # start with 1 because nums[0] is always unique
        i = 1

        for j in range(1, len(nums)):
            # check if nums[j] is unique to previous num
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1

        # return i as the number of unique elements in nums.
        return i

# 27. Remove Element
"""
How to solve?
1. Check if the element is the same as val.
2. If not same, keep this element in the list. Otherwise, remove it from the list.

Runtime is O(n).
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Initialise k
        k = 0

        # Check if the element is the same as val using for-loop.
        for i in range(len(nums)):
            # if not, keep the element in the list. Otherwise, remove it from the list.
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

# 28. Find the index of the First Occurrence in a String
"""
How to solve?
1. Check the needle in haystack.
-> range(n-m+1): Find the right position to fit the needle size.
-> Ex: haystack=abcdef, needle=cd -> i=0:ab, i=1:bc,i=2:cd,i=3:de,i=4:ef,i=5:NG(When i=5, cannot check 2 words (= the length of needle)).
-> Therefore, 6-2+1=5, for i in range(5) = i=0,1,2,3,4.
2. Compare the substring of haystack using slice.
-> Ex: haystack=abcdef, needle=cd -> haystack[0:0+2] -> ab != cd, haystack[1:1+2] -> bc != cd, haystack[2:2+2] -> cd == cd.

Runtime is O(n).
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)

        # Loop through possible starting indices
        for i in range(n - m + 1):
            # Check substring match
            if haystack[i:i + m] == needle:
                return i

        return -1

# 35. Search Insert Position
"""
How to solve?
1. Use binary search.
2. Set midpoint.
3. If midpoint < target, move left foward. 
If midpoint >=target, move right backward.
4. Repeat 2 and 3 until we find the target.
5. If not found, left is the insertion point.

Runtime is O(log n).
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # If not found, 'left' is the insertion point
        return left

# 58. Length of Last Word
"""
How to solve?
1. Split string by ""
-> split("") causes ValueError: empty separator.
2. Check only the length of the last word.

Runtime is O(n).
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # split string with empty space
        words = s.split()
        # check only the length of the last word
        if words:
          length = len(words[-1])
        # if string is empty, length is 0 (prevent IndexError)
        else:
          length = 0  

        return length

# 66. Plus one
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
