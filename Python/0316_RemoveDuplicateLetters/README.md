# [316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters)

## Description

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

```
Input: "bcabc"
Output: "abc"
```

Example 2:

```
Input: "cbacdcbc"
Output: "acdb"
```

## Solution

```
freq = Counter(s)
visited, stack = set(), []
    
for c in s:
    freq[c] -= 1
    if c not in visited:                
        while stack and c < stack[-1] and freq[stack[-1]] > 0:
            visited.remove(stack.pop())
        stack.append(c)
        visited.add(c)
    
return "".join(stack)
```

First we count the amount of each letter. And we prepare a stack to store the result and a set to store what stack contains to reduce the checking time.

After that we iterate the string. For each character, we minus its number of appearence and check if it is in the stack. If so, we just move on to the next character. Otherwise, we check if the top of the stack (say **k**) is greater than the current letter and there are some **k** remains. If so we pop **k** from the stack. And we push the current letter into the stack and remark it is in the stack. This part helps us to put smaller letters as front as possible.

Time complexity: O(n)<br>
Space complexity: O(n)

## Related Topics

[Stack](https://leetcode.com/tag/stack/) , [Greedy](https://leetcode.com/tag/greedy/) 