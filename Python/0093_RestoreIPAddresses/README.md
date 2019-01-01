# [93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses)

## Description

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

```
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
```

## Solution

We can start with checking the length of the input string. It must be no more than 13 characters because the longest valid IP address is just 12 numbers.

The we start executing our backtracking algorithm. We set up a function with variables including the remaining string **s** and a counter for the number of divisions of the IP address. In this function, we use a loop only runs three times because a part of a IP address only contains 1 to 3 characters. In the loop, we take out 1 to 3 characters separately as a division of the IP and run the same function on the remaining string. Once the counter reaches zero and the string is used of characters, we generate a valid IP address and we store it.

The time complexity of this algorithm is O(3<sup>n</sup>) which is really costly. However we eliminate those cases whose input length is greater than 12 characters, the upperbound is restricted at O(3<sup>12</sup>). The auxiliary space is also restricted by the counter so that the size of the recursive stack wouldn't excess 4. Hence the auxiliary space is constant.

## Related Topics

[String](https://leetcode.com/tag/string/) , [Backtracking](https://leetcode.com/tag/backtracking/) 

## Similar Questions

[IP to CIDR](https://leetcode.com/problems/ip-to-cidr/)
