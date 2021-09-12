# 14. Longest Common Prefix
## Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

Example 2:

```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

Constraints:

```
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
```

## Python Solution 1

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for strx in strs[1:]:
            while strx.find(prefix) != 0:
                prefix = prefix[:len(prefix)-1:]
                if prefix == '':
                    return ""
        
        return prefix
```

## Python Solution 2: Vertical scanning

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for j in range(len(strs)):
                if i == len(strs[j]) or strs[j][i] != ch:
                    return strs[0][:i]
        return strs[0]
```
