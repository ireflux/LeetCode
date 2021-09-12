# 9. Palindrome Number
## Easy

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Example 1:

```
Input: x = 121
Output: true
```

Example 2:

```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

Example 3:

```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

Example 4:

```
Input: x = -101
Output: false
```

Constraints:

```
-2^31 <= x <= 2^31 - 1
```

## Python Solution 1

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0) or ((x % 10 == 0) and (x != 0)):
            return False
        
        result = 0
        while result < x:
            result = result * 10 + x % 10
            x //= 10
        
        return (result == x) or (result // 10 == x)
```

## Golang Solution

```golang
func isPalindrome(x int) bool {
    if x < 0 || (x % 10 == 0 && x != 0){
        return false
    }
    original := x
    reversed := 0
    for x != 0{
        reversed = reversed * 10 + x % 10
        x /= 10
    }
    
    return original == reversed
}
```
