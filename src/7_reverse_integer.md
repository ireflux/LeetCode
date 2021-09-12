# 7. Reverse Integer
## Easy

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

```
Input: x = 123
Output: 321
```

Example 2:

```
Input: x = -123
Output: -321
```

Example 3:

```
Input: x = 120
Output: 21
```

Example 4:

```
Input: x = 0
Output: 0
```

Constraints:

```
-2^31 <= x <= 2^31 - 1
```

## Python Solution 1

```python
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
```

## Python Solution 2

```python
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
```

## Golang Solution

```golang
import "math"

func reverse(x int) int {
    result := 0
    symbol := 1
    if x < 0 {
        symbol = -1
        x = -x
    }else{
        symbol = 1
    }
    
    for x != 0{
        result = result * 10 + x % 10
        x /= 10
    }
    
    if float64(result) > math.Pow(2,31){
        return 0
    }
    
    return symbol * result
}
```
