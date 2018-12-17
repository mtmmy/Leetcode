# [957. Prison Cells After N Days](https://leetcode.com/problems/prison-cells-after-n-days)

## Description

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

- If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
- Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)


Example 1:

```
Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
```

Example 2:

```
Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
```

Note:

1. cells.length == 8
2. cells[i] is in {0, 1}
3. 1 <= N <= 10^9

## Solution

First, edge cells may be occupied but it must be vacant since day 1. Second, we assume that the there is a pattern of changing cells. We start updating cells from day 1 until we encounter the same permutation and remember how many updates, called K, we make during the period. And we can reduce N by take the remainder of K divided by K and only run these many iterations.

Accroding to this [disccustion](https://leetcode.com/problems/prison-cells-after-n-days/discuss/205684/JavaPython-Find-the-Loop-Mod-14), the author has done the burte-force verification that K has only 3 possbility, 1, 7, and 14. So the most iteration we need is 13 which is a constant number. Hence the time complexity is O(1). The space complexity is O(1) as well.

## Related Topics

[Hash Table](https://leetcode.com/tag/hash-table/) 
