# [406. Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height)

## Description

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

```
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
```



## Solution

Since k indicates how many eqal or higher people infront of that people, we can sort the list by height descendingly and then k ascendingly. After that, we go through the sorted list and insert each element to the new list depending on its k value. Like the example above, after sorting, we get [[7,0], [7,1], [6,1],  [5,0], [5,2], [4,4]]. And we insert [7, 0] at the 0th position of the new list because we want that there's no one in front of it. Next we put [7, 1] at 1st position. And then [6, 1], here the conflict happens. There's already [7, 1] at the 1st position. And this is the reason we sort the list by height. We can simply insert [6, 1] to the 1st position and force [7, 1] to the 2nd position which will not violate the constrain of [7, 1] that there is only one eqal of higher person in front of it.

The time complexity of this greedy approch is O(nlogn) since we need sort the queue first and the reconstructing part only takes O(n). And we need O(n) auxiliary space to store the reconstructed queue.

## Related Topics

[Greedy](https://leetcode.com/tag/greedy/) 

## Similar Questions

[Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
