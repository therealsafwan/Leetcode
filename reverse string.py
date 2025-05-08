#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define the 32-bit signed integer range
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        # Handle the sign of the number
        sign = -1 if x < 0 else 1
        x = abs(x)  # Work with the absolute value of x

        # Reverse the digits by converting the number to a string and reversing it
        reversed_x = int(str(x)[::-1]) * sign

        # Check if the reversed integer is within the 32-bit signed integer range
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0

        return reversed_x

