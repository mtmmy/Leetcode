# [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring)

## Description

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

```
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
```

Note:

- If there is no such window in S that covers all characters in T, return the empty string "".
- If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

## Solution

1. Create a counter of string **T**
2. Start a iteration on string **S** and call the iterator **right**. **right** indicates the right end of the window.
3. if s[right] is in the counter go the step 4. Otherwise, increment **right**.
4. counter[s[right]] decrese by 1. If the value still equal or greater than zero, count++ and go to step 5. Otherwise, right++ and go back to step 3.
5. If the **count** is equal to the length of string **T**, get the current window size and compare to the smallest window by far. If the current is smaller, update the result. If the **count** is not equal to the length of string **T**, go back to step 3.
6. If s[left] \(**left** indicates the left end of the window\) is in the **counter**, counter[s[left]]++. If counter[s[left]] is greater than zero, **count--**, because the current window doesn't contain all characters in string **T**.
7. **left++** and go back to step 5.
8. Return **result**.

The time complexity of this algorithm is O(N) where N is the length of string **S**. The space complexity is O(M) where M is the length of string **T**.

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) , [Two Pointers](https://leetcode.com/tag/two-pointers/) , [String](https://leetcode.com/tag/string/) 

## Similar Questions

[Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/), [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/), [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/), [Permutation in String](https://leetcode.com/problems/permutation-in-string/), [Smallest Range](https://leetcode.com/problems/smallest-range/), [Minimum Window Subsequence](https://leetcode.com/problems/minimum-window-subsequence/)
