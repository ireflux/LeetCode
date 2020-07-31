# 7. Reverse Integer
## Easy

> Given a 32-bit signed integer, reverse digits of an integer.   
> Example 1:  Input: 123   Output: 321   
> Example 2:  Input: -123  Output: -321  
> Example 3:  Input: 120   Output: 21  
> Note:  
> Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

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
