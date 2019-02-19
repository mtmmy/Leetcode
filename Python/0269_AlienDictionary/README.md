# [269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary)

## Description

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

```
Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
```

Example 2:

```
Input:
[
  "z",
  "x"
]

Output: "zx"
```

Example 3:

```
Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
```

Note:

1. You may assume all letters are in lowercase.
2. You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
3. If the order is invalid, return an empty string.
4. There may be multiple valid order of letters, return any one of them is fine.

## Solution

We consider each letter as a node and two nodes have an edge if one letter is before another in the inputs array. The one which is front has an out degree and points to the after one. We implement these connections by a set called **orderSet** who stores tuples with (front, after) structure. After that, we calculate the number of incomming edges of each node. After this step, we find those letters who don't have any incoming edge which are smallest letters lexicographically. We push these letters in a queue and append to the result string.

The we use BFS strategy from the head of the queue. For a node, we lower the incomming degrees by 1 of all its connected nodes. Once the incomming degree is zero, we push that letter into the queue and append to the result string.

Before reture, we need to check if we use all letters. If we don't, it means there are some letters' incoming degree is not zero which implys circles exist.

V: number of letters
E: number of edges (direct relation)

Time complexity: O(V + E)<br>
Space complexity: O(V + E)

## Related Topics

[Graph](https://leetcode.com/tag/graph/) , [Topological Sort](https://leetcode.com/tag/topological-sort/) 

## Similar Questions

[Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
