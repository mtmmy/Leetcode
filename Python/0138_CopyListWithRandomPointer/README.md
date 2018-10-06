# [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer)

## Description

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

## Solution

The visual representation of this kind of linked list may look like the picture on [GeeksforGeeks](https://www.geeksforgeeks.org/a-linked-list-with-next-and-arbit-pointer/).

First, we create a copy node for each node and point it from the original node like this:

```
A -> B -> C -> D
|    |    |    |
|   null  |    +--> A 
|         |
+--> C    +--> B

to

A -> A' -> B -> B' -> C -> C' -> D -> D'
|          |          |          |
|         null        |          +--> A
|		                  |
+--> C                +--> B
```
The horizontal arrows represent next, and go-down arrows represent random.  

Secondly, we copy the random pointers to the coressponding copied nodes. For example, the random pointer of A' points to C', so that of C' points to B' etc.

Now we have two identical linked lists only entangled together. After seperating them, we get a deep copy list from the orignal one.
