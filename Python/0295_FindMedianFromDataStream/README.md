# [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream)

## Description

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

 

Example:

```
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
```

Follow up:

1. If all integer numbers from the stream are between 0 and 100, how would you optimize it?
2. If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

## Solution

My first thought is to maintain a sorted list which allows us easily to find the median. However this approach is costly. Even though I use binary search to find the place to insert the new number, the insertion still takes O(n) time and with the binary search, it's O(n log n) totally for everytime addNum() is called.

But when we are looking for the median, we only care the middle number if total numbers is odd or the middle two number if total numbers is even. So maintaining a sorted array gives us to much information along with too high cost. Thus we maintain two heaps, one is min heap to store the bigger half of numbers, **highHeap**; the other is max heap to store the smaller half of numbers **lowHeap**.

The main idea is that we keep two heaps balanced. When a new number comes in, we check which side it should be and put it into the corresponding heap. And we check the size of two heaps, if the difference of their size is over 1, we blance them. If **highHeap** is bigger, we pop the smallest number from it and put that number into **lowHeap** and vise versa. 

For addNum():<br>
Time complexity: O(log n)

## Related Topics

[Heap](https://leetcode.com/tag/heap/) , [Design](https://leetcode.com/tag/design/) 

## Similar Questions

[Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)
