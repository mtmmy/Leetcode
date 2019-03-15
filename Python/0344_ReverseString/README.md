# [344. Reverse String](https://leetcode.com/problems/reverse-string)

## Description

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:

```
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

Example 2:

```
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

## Solution

We use two pointers point the head and the tail and move points to the middle of the array followed by swapping string of these two pointers pointed.

Time complexity: O(n)<br>
Space complexity: O(1)

```
i, j = 0, len(s) - 1
        
while i < j:
    s[i], s[j] = s[j], s[i]
    i += 1
    j -= 1
```

## Related Topics

[Two Pointers](https://leetcode.com/tag/two-pointers/) , [String](https://leetcode.com/tag/string/) 

## Similar Questions

[Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/), [Reverse String II](https://leetcode.com/problems/reverse-string-ii/)
