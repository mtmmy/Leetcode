# [207. Course Schedule](https://leetcode.com/problems/course-schedule)

## Description

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

```
Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
```

Example 2:

```
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
```

Note:

1. The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
2. You may assume that there are no duplicate edges in the input prerequisites.

## Solution

At the begining, we create two hash tables. One is how many prerequisites for each course; another is what courses we can take after finished a course. This setting considers all courses as vertices and the prerequisites as edges of a graph. Hence if a node has incoming edges, it has some prerequisites.

After that, we put all nodes which don't have any incoming edges (courses without prerequisites) into a queue and process them one by one. When we processing it, we get all its connected nodes by outgoing edges, decrement their incoming edge (remove the edge) and put nodes if their incoming degree is zero after removing the edge. We keep doing this process until queue is empty.

Finally, we check the incoming degree of each nodes. If there is any node whose degree is not zero, the schedule dosen't work. Otherwise it's a valid schedule.

Time complexity: O(V + E). Since we visit every vertex and edges once. <br>
Space compelxity: O(V + E). In the **dictPre** hash table, we stores all nodes and their edges.

## Related Topics

[Depth-first Search](https://leetcode.com/tag/depth-first-search/) , [Breadth-first Search](https://leetcode.com/tag/breadth-first-search/) , [Graph](https://leetcode.com/tag/graph/) , [Topological Sort](https://leetcode.com/tag/topological-sort/) 

## Similar Questions

[Course Schedule II](https://leetcode.com/problems/course-schedule-ii/), [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/), [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/), [Course Schedule III](https://leetcode.com/problems/course-schedule-iii/)
