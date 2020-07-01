#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# 58. Length of Last Word
# Easy

# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
# If the last word does not exist, return 0.
# Note: A word is defined as a maximal substring consisting of non-space characters only.
# Example: Input: "Hello World"  Output: 5

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length,tail = 0,len(s) - 1
        while (tail >= 0 and s[tail] == ' '):
            tail -= 1
        while (tail >= 0 and s[tail] != ' '):
            length += 1
            tail -= 1
        
        return length