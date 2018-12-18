# [68. Text Justification](https://leetcode.com/problems/text-justification)

## Description

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

Example 1:

```
Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

Example 2:

```
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
```

Example 3:

```
Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```

## Solution

We use the algorithm as follows:

1. Orgnize words to lines accroding to the maximum width
2. Fill up blanks for every line

This is a high-level algorithm. Now let's get into details. For the first step, we execute the following steps:

1. If remainWidth >= len(word), we append that word and a blank to the line and decrease **remainWidth** by **len(word) + 1** (extra one because of the blank).
2. Otherwise, we create a new line and put the word and a blank to this new line. Set **remainWidth** as **maxWidth - len(word) - 1**.

The detail of the second step is as follows:

1. If the **lineWidth** is smaller than **maxWidth** and the line contains more than 1 word, we need seperate them by equal amount of blank if possible. If it's not possible, only the last gap can be waived.
2. If the line only contains one word, we algin that word to the left and fillup blanks for the rest of the line.
3. For the last line, we need to align words to the left and seperate them by one blank and fill up the whole line by blanks.

Let's say **N** is the amount of given words, we need O(N) to organize words to lines, and another O(N) to refill blanks. Hence the time complexity is O(N). The space complexity is also O(N).

## Related Topics

[String](https://leetcode.com/tag/string/) 