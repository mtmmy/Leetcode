# [336. Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs)

## Description

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

```
Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
```

Example 2:

```
Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
```

## Solution

The straightfoward solution is to combine every two words and check if the new string is palindromic. However this approach takes significantly high computation time. It takes O(n<sup>2</sup> * l) where n is the number of words and l is the max length of words.

```
def isPalindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1                
    return True

result, n = [], len(words)
pos, length = {}, set()
    
for i in range(n):
    pos[words[i]] = i
    length.add(len(words[i]))
    
sortedLength = sorted(list(length))
for i in range(n):
    rWord = words[i][::-1]
    if rWord in pos and pos[rWord] != i:
        result.append([i, pos[rWord]])
    
    wLen = len(rWord)
    for l in sortedLength:
        if l == wLen:
            break
        if isPalindrome(rWord, 0, wLen - l - 1) and rWord[wLen - l:] in pos:
            result.append([i, pos[rWord[wLen - l:]]])
        if isPalindrome(rWord, l, wLen - 1) and rWord[:l] in pos:
            result.append([pos[rWord[:l]], i])

return result
```

Hence we need to use some data structures to help us reducing the cost of time. The hash table helps because we can find the target word in O(1) time. So the next step is, we need a method to find what can make current string into a palindrome. When we generate the hash table we mentioned before, we record words' locations as the key. The hash table is called **pos** in the code. And we also use a set to keep lengthes of all words.

And then we go thorugh every words. First we reverse the word. And we find if the reversed word is in the **pos**. If so, we add the pair to the result. When we add the result, we only add one side. For example, "abcd" and "dcba", they can be merged into a palindrome no matter who's at the first. The reason of adding one side is when the loop reachs "dcba", it will take care the reversed part.

After taking care the same length situation, we still need to check two words with different length. At the first part, we store the lengthes to a set. Now we use a loop to go through elements in it. We can consider this as "is there a word with length **L** which can merge with the current word and form a palindrom?" And this loop stops when the **L** is as long as the length of the current word. For example, "a" and "aaa", we will not find this two words form palindroms when the loop is on "a", but we will find out eventually when the loop arrives at "aaa", so there will be no miss. 

In the loop, we have to if statements as follows:

```
if isPalindrome(rWord, 0, wLen - l - 1) and rWord[wLen - l:] in pos:
    result.append([i, pos[rWord[wLen - l:]]])
if isPalindrome(rWord, l, wLen - 1) and rWord[:l] in pos:
    result.append([pos[rWord[:l]], i])
```

the first one we check if rWord[0:wLen - 1 - 1] is palindromic and  if **pos** contains the word rWord[wLen - 1:] (remember rWord is already reversed.) If they both are true, it means curWord + targetWord is palindromic. The second if is the same idea just take the tail part.

Time complexity: O(n * l<sup>2</sup>)<br>
Space complexity: O(n)

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) , [String](https://leetcode.com/tag/string/) , [Trie](https://leetcode.com/tag/trie/) 

## Similar Questions

[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/), [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/)
