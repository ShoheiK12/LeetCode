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

        # Loop by the end of list
        while current and current.next:
            # If current value = next value of current, skip the next -> current.next = current.next.next
            if current.val == current.next.val:
                current.next = current.next.next
            # If the values are different, move pointer(current)
            else:
                current = current.next
        
        return head
