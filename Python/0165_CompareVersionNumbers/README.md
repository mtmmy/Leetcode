# [165. Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers)

## Description

Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Example 1:

```
Input: version1 = "0.1", version2 = "1.1"
Output: -1
```

Example 2:

```
Input: version1 = "1.0.1", version2 = "1"
Output: 1
```

Example 3:

```
Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
```

Note:

1. Version strings are composed of numeric strings separated by dots . and this numeric strings may have leading zeroes.
2. Version strings do not start or end with dots, and they will not be two consecutive dots.

## Solution

First we convert two version numbers into two int list. We compare two lists number by number from heads. If there is a different number, we can return the result a this stage. Otherwise we check the tracking numbers, if there is any number greater than 0, then we know the version is different. Otherwise the two version is the same.

Time complexity: O(n)<br>
Space complexity: O(n)


## Related Topics

[String](https://leetcode.com/tag/string/) 