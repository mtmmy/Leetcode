# [218. The Skyline Problem](https://leetcode.com/problems/the-skyline-problem)

## Description

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

![](https://leetcode.com/static/images/problemset/skyline1.jpg)![](https://leetcode.com/static/images/problemset/skyline2.jpg)

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

- The number of buildings in any input list is guaranteed to be in the range [0, 10000].
- The input list is already sorted in ascending order by the left x position Li.
- The output list must be sorted by the x position.
- There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]


## Solution

Solution 1:

First we find the top-left point and the right-bottom point of each building as default critical points. After that we sort them by their x position in ascending order. Next, we want to eliminate points who is being blocked by other buildings with the following pseudocode.

```
for each buliding b:
	for each critical point c:
		if c.y < b.h and c.x >= b.l and c.x < b.r:
			c.y = b.h
```

After this step, we update those covered points with higher buildings. The last step is eliminate with the same height.

Time complexity: O(n<sup>2</sup>)
Space complexity: O(n)

Solution 2:

We first create a list with all buildings and append right-bottom points of each builing with (R, None, 0) format. And we sort this array. Later we setup a heap with (-y, x) for storing critical points.

Now we start going through the **sortedBuilding** list. For each building, we only concern points that their x position are greater than the x position of the building, thus we can remove those x are smaller points from the heap. If we meet a new height, we push its (H, R) into the heap. This point of (H, R) will be the compared point ignoring point c that c.x < R and c.h < H and adding points that c.x < R and c.h > H. Last we only need check if the current critical point has the same height of the previous one. If not so, we append the new point to the result.

We only need O(n log n) for sorting and O(n log n) for looping depending on operations of a heap (O(log n). Hence totally it's O(n log n).

Space complexity: O(n).

## Related Topics

[Divide and Conquer](https://leetcode.com/tag/divide-and-conquer/) , [Heap](https://leetcode.com/tag/heap/) , [Binary Indexed Tree](https://leetcode.com/tag/binary-indexed-tree/) , [Segment Tree](https://leetcode.com/tag/segment-tree/) 

## Similar Questions

[Falling Squares](https://leetcode.com/problems/falling-squares/)
