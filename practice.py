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
