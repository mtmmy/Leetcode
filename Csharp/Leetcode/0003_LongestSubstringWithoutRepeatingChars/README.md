# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)

## Description

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

## Solution
First, we create a container to keep the last index of the apperence for each characters. Secondly, we create a varaible to keep our start point for every time we calculate the lenght of substring. Afterword, we start looping the target string. In the interation, we first compare the last apperence of the current character and the current starting point and pick the greater one. If the starting point is less than the last apperence of the current character, it means the current character repeats so that we need counting our substring from the index of the last apperence of the current character plus one. And then we update the last index of the current character. The final step we update the longest value.
