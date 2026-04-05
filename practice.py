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
