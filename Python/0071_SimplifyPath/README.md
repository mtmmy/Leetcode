# [71. Simplify Path](https://leetcode.com/problems/simplify-path)

## Description

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
path = "/a/../../b/../c//.//", => "/c"
path = "/a//b////c/d//././/..", => "/a/b/c"

In a UNIX-style file system, a period ('.') refers to the current directory, so it can be ignored in a simplified path. Additionally, a double period ("..") moves up a directory, so it cancels out whatever the last directory was. For more information, look here: https://en.wikipedia.org/wiki/Path_(computing)#Unix_style

Corner Cases:

- Did you consider the case where path = "/../"?
In this case, you should return "/".
- Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

## Solution

We can implement the algorithm by stack. First of all, we split the path string by characters "/". After that, there are three conditions. First, when we encounter "..", we need to remove the folder before it which is equal to popping the element from the stack. Second, when we meet empty strigs or ".", we just do nothing. Last, we see any valid folder name, we push it to the stack.

After consumming the string, we have simplified folder names in order in the stack. We just join them with the character "/". The time complexity is O(N) and N is the number of elements in the path string.

## Related Topics

[String](https://leetcode.com/tag/string/) , [Stack](https://leetcode.com/tag/stack/) 