#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# 7. Reverse Integer

# Given a 32-bit signed integer, reverse digits of an integer.
# Example 1:  Input: 123   Output: 321
# Example 2:  Input: -123  Output: -321
# Example 3:  Input: 120   Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

# 1
class Solution:
    def reverse(self, x: int) -> int:
      result = 0
      if x < 0:
        symbol = -1
        x = -x
      else:
        symbol = 1
        
      while x:
        result = result * 10 + x % 10
        x //= 10

      if result > pow(2,31):
        return 0
      
      return symbol * result


# 2
class Solution:
    def reverse(self, x: int) -> int:
      symbol = 1
      if x < 0:
        symbol = -1
        strx = str(x)[1:]
      else:
        strx = str(x)
        
      result = int(strx[::-1])

      if result > pow(2,31):
        return 0
      
      return symbol * result