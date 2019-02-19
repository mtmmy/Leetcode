# [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum)

## Description

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

```
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?

## Solution

We use a queue to store the index within the sliding window and use a loop to go through **nums** list. In the loop, we do the following algorithm:

```
if queue and queue[0] == i - k:
    queue.popleft()
while queue and nums[queue[-1]] < nums[i]:
    queue.pop()
queue.append(i)
if i >= k - 1:
    result.append(nums[queue[0]])
```

The first if statement is removing the element from the sliding window if that element has not been covered. The while statement help us removing all smaller value which we don't concern and keep the larget value of the sliding window at the first place of the queue. The second if statement stroe the largest value of each sliding window.

Time complexity: O(n)<br>
Space complexity: O(k)

## Related Topics

[Heap](https://leetcode.com/tag/heap/) 

## Similar Questions

[Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/), [Min Stack](https://leetcode.com/problems/min-stack/), [Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/), [Paint House II](https://leetcode.com/problems/paint-house-ii/)
