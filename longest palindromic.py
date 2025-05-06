# Given a string s, return the longest palindromic substring in s.
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        # Helper function to expand around center
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # the longest palindrome in the current range

        longest_palindrome = ""

        for i in range(len(s)):
            # Odd length palindrome (expand around a single character)
            palindrome1 = expand_around_center(i, i)
            # Even length palindrome (expand around a pair of characters)
            palindrome2 = expand_around_center(i, i + 1)

            # Choose the longer palindrome
            if len(palindrome1) > len(longest_palindrome):
                longest_palindrome = palindrome1
            if len(palindrome2) > len(longest_palindrome):
                longest_palindrome = palindrome2

        return longest_palindrome
