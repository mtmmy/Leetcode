# [159. Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters)

## Description

Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

```
Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
```

Example 2:

```
Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
```

## Solution

Solution 1:

We use a set to store characters we've met and the size of this set is up to 2. And we use the variable **counter** to count the length of the substring. If the size of **twoChars** is less than 2, we keep increasing **counter**. And the variable **i**, its position is changed when the pointer **j** meets a different character which means the pointer **i** always points the last kind of character of the current substring. Furthermore, when **twoChars** is full and the pointer **j** meets the third kind of character, we update it by characters that **i** and **j** point.

Time complexity: O(n)<br>Space complexity: O(1)

Solution 2:

In this solution, we use three pointers, **fstHead**, **fstTail**, and **tracker**. **tracker** keeps checking whether the character changes no not. If it changes and **fstTail** is not -1 (means the new character we meet is the third kind of character), we update the max length if needed. 

Time complexity: O(n)<br>Space complexity: O(1)

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) , [Two Pointers](https://leetcode.com/tag/two-pointers/) , [String](https://leetcode.com/tag/string/) 

## Similar Questions

[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/), [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/), [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)
