"""
LeetCode 9
Problem Name: Palindrome Number

Definition:
A palindrome number reads the same from left to right and right to left.

Example:
121 -> Palindrome
123 -> Not Palindrome

Approach:
1. Store the original number.
2. Reverse the number.
3. Compare the original number with the reversed number.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers cannot be palindrome
        if x < 0:
            return False

        original = x
        reverse = 0

        while x > 0:
            last_digit = x % 10
            reverse = reverse * 10 + last_digit
            x = x // 10
        return original == reverse