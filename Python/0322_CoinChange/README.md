# [322. Coin Change](https://leetcode.com/problems/coin-change)

## Description

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

```
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
```

Example 2:

```
Input: coins = [2], amount = 3
Output: -1
```

Note:
You may assume that you have an infinite number of each kind of coin.

## Solution

DP:

We create an array with the length of (**amount** + 1) called **coinCount** where **coinCount[i]** denotes the minimum coins requires for amount **i**. And we initailize elements in this array with **amount** + 1 (could be any number greater than the amoun) except **coinCount[0]** which is 0. And for each element in **coinCount**, we try out every kind of coins and use the following method to update the value:

```
coinCount[i] = min(coinCount[i], coinCount[i - coin] + 1)
```

Last, the last element of **coinCount** is the answer if the value of it is smaller or equal to the amount; otherwise return -1.

Tiem complexity: O(n * amount)<br>
Sapce compelxity: O(n)

```
coinCount = [amount + 1] * (amount + 1)
coinCount[0] = 0
for i in range(1, amount + 1):
    for coin in coins:
        if coin <= i:
            coinCount[i] = min(coinCount[i], coinCount[i - coin] + 1)

return -1 if coinCount[-1] > amount else coinCount[-1]
```

DFS:

Intuitively, we try the coin with the highest value first if we confront this problem in real life. Hence we can develop based on this intuition. We first sort coins in descending order and start the DFS function. In the DFS function, there is a for loop. We can think it as that we take one coin and try another kind of coin, and then two coins, three coins and so on. We also setup different conditions to terminate the search as early as possible.

```
if remain < 0:
    return
if count - (-remain // coins[coinIdx]) > self.result:
    return
if remain % coins[coinIdx] == 0:
    self.result = min(self.result, count + remain // coins[coinIdx])
if coinIdx == len(coins) - 1:
    return
for i in range((remain // coins[coinIdx]), -1, -1):
    dfs(remain - i * coins[coinIdx], count + i, coinIdx + 1)
```

The first if means the total coins we get has exceed the amount. The second condition means there is no possible way we can use less coins than the current result since the coin are used in descending order. And (remain // coins[coinIdx]) is the fewest possible number of coins we can take. The third if is straightfoward. The fourth one is because it's the last coin and there is no next level. 


## Related Topics

[Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) 