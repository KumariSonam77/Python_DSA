"""
LeetCode 2520
Problem Name: Count the Digits That Divide a Number

Definition:
Count how many digits completely divide the given number.

Example:
Input = 121

Digits:
1
2
1

121 % 1 = 0
121 % 2 = 1
121 % 1 = 0

Answer = 2

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution(object):
    def countDigits(self, num):

        original = num
        count = 0
        while num > 0:
            digit = num % 10
            if original % digit == 0:
                count += 1
            num = num // 10
        return count
# Test
obj = Solution()
print(obj.countDigits(121))