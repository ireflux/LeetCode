#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# 9. Palindrome Number

# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# Example 1: Input: 121  Output: true
# Example 2: Input: -121 Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3: Input: 10   Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0) or ((x % 10 == 0) and (x != 0)):
            return False
        
        result = 0
        while result < x:
            result = result * 10 + x % 10
            x //= 10
        
        return (result == x) or (result // 10 == x)