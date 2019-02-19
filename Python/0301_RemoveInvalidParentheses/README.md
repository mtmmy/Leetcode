# [301. Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses)

## Description

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

```
Input: "()())()"
Output: ["()()()", "(())()"]
```

Example 2:

```
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
```

Example 3:

```
Input: ")("
Output: [""]
```

## Solution

BFS:

```
def isValid(s1):
    count = 0
    for c in s1:
        if c == "(":
            count += 1
        elif c == ")":
            count -= 1
            if count < 0:
                return False
    return count == 0
    
result, queue, visited, found = [], deque([s]), set(), False
    
while queue:
    curStr = queue.popleft()
    if isValid(curStr):
        result.append(curStr)
        found = True
    if not found:
        for i in range(len(curStr)):
            c = curStr[i]
            if c == "(" or c == ")":
                tempStr = curStr[:i] + curStr[i + 1:]
                if tempStr not in visited:
                    queue.append(tempStr)
                    visited.add(tempStr)
return result
```   

We first create a function to check if the string is valid. Later we use BFS approach to find all valid string with minimum deletions. If the current level is not valid, we remove one of parentheses and append this new string to the queue for the next level. Here we use a set to keep visited string to reduce calculation time.

Time complexity (say n is the length of s) : 

```
T(n) = n * C(n, n) + (n - 1) * C(n, n - 1) + ... + 1 * C(n, 1)
     = n * 2^(n-1)
```

Space complexity: O(2<sup>n</sup>)


DFS:

```
def searchValidParentheses(s, last_i, last_j, p, result):        
    count = 0
    for i in range(last_i, len(s)):
        if s[i] == p[0]:
            count += 1
        elif s[i] == p[1]:
            count -= 1
        
        if count >= 0:
            continue
        
        for j in range(last_j, i + 1):
            if s[j] == p[1] and (j == last_j or s[j] != s[j - 1]):
                searchValidParentheses(s[:0 + j] + s[j + 1:], i, j, p, result)
        return

    reverse = s[::-1]
    if p[0] == '(':
        searchValidParentheses(reverse, 0, 0, [')', '('], result)
    else:
        result.append(reverse)
result = []
searchValidParentheses(s, 0, 0, ['(', ')'], result)
return result
```

In the first part of **searchValidParentheses** which is a recursive function, we find extra right parenthese and remove it and then go to the next layer. If the right parentheses is equal or less than the left one, the program will go through the for loop. And we reverse the string and the checker **p**, to remove the extra left parentheses. If some string can pass loops in the original order and reversed order, than it's a valid string.

Time complexity and space complexity are same as in BFS.

## Related Topics

[Depth-first Search](https://leetcode.com/tag/depth-first-search/) , [Breadth-first Search](https://leetcode.com/tag/breadth-first-search/) 

## Similar Questions

[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
