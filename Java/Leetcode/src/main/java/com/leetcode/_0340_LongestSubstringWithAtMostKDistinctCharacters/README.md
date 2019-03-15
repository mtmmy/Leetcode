# [340. Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters)

## Description

Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

```
Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
```

Example 2:

```
Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
```

## Solution

Here we use the sliding window approach along with a hash table. The hash table will count the amount of characters within the window. And we go through the input string and count the number of each character. Every time we count a character, we check the size of the hash table. If the size of the hash exceed the number **k**, we need to remove the character at the index **j** which is the beginning of the window from the hash table until the size of hash table is **k**. And the length of the current substring with k distinct characters is **i - j**. We use a variable to track the maximum of this kind of substrings.

Time complexity: O(n)<br>
Space complexity: O(n)

```
public int lengthOfLongestSubstringKDistinct(String s, int k) {
    int maxLen = 0, j = -1;
    Map<Character, Integer> charCount = new HashMap<>();

    for (int i = 0; i < s.length(); i++) {
        char cur = s.charAt(i);
        int curCount = charCount.getOrDefault(cur, 0);
        charCount.put(cur, curCount + 1);

        while (charCount.size() > k) {
            char charJ = s.charAt(++j);
            int tempCount = charCount.get(charJ);
            charCount.put(charJ, tempCount - 1);
            if (tempCount - 1 == 0) {
                charCount.remove(s.charAt(j));
            }
        }
        maxLen = Math.max(maxLen, i - j);
    }
    return maxLen;
}
```

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) , [String](https://leetcode.com/tag/string/) 

## Similar Questions

[Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/), [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
