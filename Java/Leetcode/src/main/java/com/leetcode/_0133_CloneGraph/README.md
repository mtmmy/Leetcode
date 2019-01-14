# [133. Clone Graph](https://leetcode.com/problems/clone-graph)

## Description

Given the head of a graph, return a deep copy (clone) of the graph. Each node in the graph contains a label (int) and a list (List[UndirectedGraphNode]) of its neighbors. There is an edge between the given node and each of the nodes in its neighbors.


OJ's undirected graph serialization (so you can understand error output):
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
 

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

1. First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
2. Second node is labeled as 1. Connect node 1 to node 2.
3. Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.

Visually, the graph looks like the following:

```
       1
      / \
     /   \
    0 --- 2
         / \
         \_/
```

Note: The information about the tree serialization is only meant so that you can understand error output if you get a wrong answer. You don't need to understand the serialization to solve the problem.

## Solution

Here we use BFS to conquer this problem. We first create a hash to store nodes in the new graph whose key is the label of the node. And we start BFS process, for each node in the original graph, we find its all neigbors and copy and store them to the hash if they are not in the hash. And we add those copied neighbor nodes to the node as its neighbors. By using a hash to store all new nodes and retrive them when we need them, we can prevent creating duplicate nodes.

The time complexity is O(V+E) where V is the number of vertices and E is the number of edges. Because we need to go through every vertex and visit every its edge once. The space complexity is O(V) since we need to clone a new same graph.

## Related Topics

[Depth-first Search](https://leetcode.com/tag/depth-first-search/) , [Breadth-first Search](https://leetcode.com/tag/breadth-first-search/) , [Graph](https://leetcode.com/tag/graph/) 

## Similar Questions

[Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)
