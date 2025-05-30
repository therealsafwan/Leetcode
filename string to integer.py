#implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

#The algorithm for myAtoi(string s) is as follows:

#Whitespace: Ignore any leading whitespace (" ").
#Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
#Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
#Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Trim leading whitespaces
        s = s.lstrip()

        if not s:
            return 0

        # Step 2: Determine the sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # Step 3: Convert the number, ignoring leading zeros
        num = 0
        for char in s:
            if not char.isdigit():
                break
            num = num * 10 + int(char)

        # Step 4: Apply the sign
        num *= sign

        # Step 5: Clamp the result within the 32-bit signed integer range
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
