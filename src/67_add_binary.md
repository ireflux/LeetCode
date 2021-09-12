# 67. Add Binary
## Easy

Given two binary strings a and b, return their sum as a binary string.

Example 1: 

```
Input: a = "11", b = "1"
Output: "100"
```

Example 2:

```
Input: a = "1010", b = "1011"
Output: "10101"
```

## Python Solution

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result, carry, list_a, list_b = '', 0, list(a), list(b)
        
        while list_a or list_b or carry:
            if list_a:
                carry += int(list_a.pop())
            if list_b:
                carry += int(list_b.pop())
                
            result += str(carry % 2)
            carry //= 2
            
        return result[::-1]
```