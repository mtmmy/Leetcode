# [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle)

## Description

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

## Solution

Here we use fast and slow pointer to go through the linked list. The faster one is  double the speed of the slower one. If there is a cycle, they will meet each other at some node in the cycle. The solution spends O(n) and only takes O(1) auxiliary space.

But why are those two pointer guaranteed meeting in the cycle?

Let say the length of tail part is T, that of cycle part is C. When the slower reaches the begining node of the cycle, it takes T steps and the faster is r nodes ahead from slower. So we can know T = kC + r where 0 <= r < C. Assuming r != 0, the slower takes C - r steps and the slower is at C - r node. Meanwhile the faster also takes 2(C - r) steps and it starts from r so now the faster is at r + 2(C - r) which is 2C - r. Hence both at the node C - r.