#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# 2. Add Two Numbers
# Medium

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example:  Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)  Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        p,q,curr = l1,l2,dummyHead
        carry = 0
        while (p or q):
            x = p.val if p else 0
            y = q.val if q else 0
            s = carry + x + y
            carry = s // 10
            curr.next = ListNode(s % 10)
            curr = curr.next
            if p:
                p = p.next
            if q:
                q = q.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummyHead.next